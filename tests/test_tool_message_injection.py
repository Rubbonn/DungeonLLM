"""
Test: ToolMessage injection into message history

Verifica se è possibile iniettare i risultati di un executor node nella message history
usando un ToolMessage (con tool_call_id fittizio). Se questo approccio fallisce,
riprova con la coppia AIMessage + ToolMessage (con ID corrispondente).

Esecuzione:
    python -m pytest tests/test_tool_message_injection.py -s
    python tests/test_tool_message_injection.py
"""

import sys
import os
import uuid
from typing import cast, Any

# Ensure the project root is on the path when running directly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.entities.creatures import Player
from app.entities.features import AbilityType, Ability, Size
from app.types.planning import Plan
from app.types.state import State
from app.nodes.nodes import executor
from app.prompts import SYSTEM_PROMPT, PLANNER_PROMPT
from app.tools import make_player_tools
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

# ---------------------------------------------------------------------------
# Ollama cloud credentials
# Override via environment variables; defaults provided for convenience.
# ---------------------------------------------------------------------------
OLLAMA_API_KEY = os.getenv(
	"OLLAMA_API_KEY",
	"c43f7a0fc49149caacf9441aad361596.32pPC8XYkS-OxiUy5WSuDcaT",
)
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "https://ollama.com")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3.5:397b-cloud")


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

def _make_test_player() -> Player:
	"""Create a test Player with all abilities set to 10 (modifier = 0)."""
	return Player(
		name="Test Player",
		size=Size.MEDIUM,
		abilities={ability: Ability(name=ability, value=10) for ability in AbilityType},
	)


def _make_initial_messages() -> list:
	"""Return a minimal conversation that should trigger a Strength ability check."""
	return [
		SystemMessage(content=SYSTEM_PROMPT),
		HumanMessage(content="Cerco di sfondare la porta con la forza bruta."),
	]


def _create_model():
	"""Instantiate the Ollama cloud model with the provided credentials."""
	return init_chat_model(
		model=OLLAMA_MODEL,
		model_provider="ollama",
		base_url=OLLAMA_BASE_URL,
		api_key=OLLAMA_API_KEY,
	)


def _run_planner(state: State) -> Plan:
	"""Run the planner agent and return the resulting Plan."""
	agent = create_agent(
		model=_create_model(),
		system_prompt=PLANNER_PROMPT,
		response_format=Plan,
	)
	response = agent.invoke(cast(Any, {"messages": state["messages"]}))
	return response["structured_response"]


def _run_send_message(state: State) -> dict:
	"""Run the send_message agent and return its output dict."""
	agent = create_agent(
		model=_create_model(),
		tools=make_player_tools(state),
		system_prompt=SYSTEM_PROMPT,
	)
	response = agent.invoke(cast(Any, {"messages": state["messages"]}))
	return {"messages": response["messages"]}


def _build_results_text(plan: Plan) -> str:
	return "\n".join(
		f"- [{a.action}] {a.reason}: {a.result}" for a in plan.actions
	)


def _mechanical_results_content(results_text: str) -> str:
	return (
		"[MECHANICAL RESULTS - use these to inform your narration, "
		f"do not expose them directly]\n{results_text}"
	)


# ---------------------------------------------------------------------------
# Main test
# ---------------------------------------------------------------------------

def test_tool_message_injection():
	"""
	Run the planner → executor pipeline, then test two injection strategies:

	Test A — ToolMessage con ID fittizio puro:
	    Aggiunge un ToolMessage senza un AIMessage corrispondente.

	Test B — AIMessage + ToolMessage coppia completa (solo se A fallisce):
	    Aggiunge prima un AIMessage con tool_calls, poi il ToolMessage con lo stesso ID.
	"""
	player = _make_test_player()
	base_messages = _make_initial_messages()

	# ------------------------------------------------------------------
	# Step 1: Run planner to get a real Plan
	# ------------------------------------------------------------------
	print("\nRunning planner…")
	state: State = {"messages": base_messages, "player": player, "plan": None}
	plan = _run_planner(state)
	print(f"Plan generated: {plan}")

	assert len(plan.actions) > 0, (
		"Planner did not generate any actions for the door-forcing scenario. "
		"Cannot proceed with injection test."
	)

	# ------------------------------------------------------------------
	# Step 2: Run executor (dice rolls, no LLM required)
	# ------------------------------------------------------------------
	state["plan"] = plan
	executor_result = executor(state)
	if "plan" in executor_result:
		state["plan"] = executor_result["plan"]

	print(f"Executor results: {state['plan']}")

	results_text = _build_results_text(state["plan"])
	print(f"Results text:\n{results_text}")

	# ------------------------------------------------------------------
	# Test A: ToolMessage with a fake tool_call_id (no matching AIMessage)
	# ------------------------------------------------------------------
	test_a_passed = False
	test_a_error = None

	print("\n=== TEST A: ToolMessage con ID fittizio ===")
	try:
		fake_id = str(uuid.uuid4())
		tool_msg_a = ToolMessage(
			content=_mechanical_results_content(results_text),
			tool_call_id=fake_id,
			name="executor",
		)

		state_a: State = {
			"messages": list(base_messages) + [tool_msg_a],
			"player": player,
			"plan": state["plan"],
		}

		response_a = _run_send_message(state_a)

		assert response_a is not None
		assert "messages" in response_a
		assert len(response_a["messages"]) > 0
		response_content = response_a["messages"][-1].content
		assert response_content and len(response_content.strip()) > 0

		test_a_passed = True
		print("[PASS] ToolMessage con ID fittizio funziona!")
		print(f"Risposta GM (anteprima): {response_content[:300]}")

	except Exception as exc:
		test_a_error = exc
		print(f"[FAIL] ToolMessage con ID fittizio ha fallito: {type(exc).__name__}: {exc}")

	# ------------------------------------------------------------------
	# Test B: AIMessage + ToolMessage coppia completa (only if A failed)
	# ------------------------------------------------------------------
	test_b_passed = False
	test_b_error = None

	if not test_a_passed:
		print("\n=== TEST B: AIMessage + ToolMessage coppia completa ===")
		try:
			call_id = str(uuid.uuid4())
			ai_msg = AIMessage(
				content="",
				tool_calls=[{"id": call_id, "name": "executor", "args": {}}],
			)
			tool_msg_b = ToolMessage(
				content=_mechanical_results_content(results_text),
				tool_call_id=call_id,
				name="executor",
			)

			state_b: State = {
				"messages": list(base_messages) + [ai_msg, tool_msg_b],
				"player": player,
				"plan": state["plan"],
			}

			response_b = _run_send_message(state_b)

			assert response_b is not None
			assert "messages" in response_b
			assert len(response_b["messages"]) > 0
			response_content_b = response_b["messages"][-1].content
			assert response_content_b and len(response_content_b.strip()) > 0

			test_b_passed = True
			print("[PASS] AIMessage + ToolMessage coppia funziona!")
			print(f"Risposta GM (anteprima): {response_content_b[:300]}")

		except Exception as exc:
			test_b_error = exc
			print(f"[FAIL] AIMessage + ToolMessage coppia ha fallito: {type(exc).__name__}: {exc}")

	# ------------------------------------------------------------------
	# Final report
	# ------------------------------------------------------------------
	print("\n=== RISULTATO FINALE ===")
	if test_a_passed:
		print("Approccio consigliato: Test A — ToolMessage con ID fittizio")
	elif test_b_passed:
		print("Approccio consigliato: Test B — AIMessage + ToolMessage coppia completa")
		print(f"(Test A fallito con: {type(test_a_error).__name__}: {test_a_error})")
	else:
		print("Entrambi gli approcci hanno fallito!")
		print(f"Test A errore: {type(test_a_error).__name__}: {test_a_error}")
		print(f"Test B errore: {type(test_b_error).__name__}: {test_b_error}")
		raise AssertionError(
			f"Entrambi i test di iniezione hanno fallito. "
			f"Test A: {test_a_error} | Test B: {test_b_error}"
		)


# ---------------------------------------------------------------------------
# Entry point for direct execution
# ---------------------------------------------------------------------------
if __name__ == "__main__":
	test_tool_message_injection()
