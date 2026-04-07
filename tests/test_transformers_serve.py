"""
Integration tests for the `transformers serve` backend.

These tests verify that DungeonLLM works end-to-end with the OpenAI-compatible
local server exposed by `transformers serve` (https://huggingface.co/docs/transformers/serve-cli/serving.md).

Prerequisites
-------------
1. Install serving dependencies::

       pip install "transformers[serving]" langchain-openai

2. Download and start the server with an instruction-tuned model that
   supports tool / function calling (tool_calls) and structured output.
   A 1-7 B parameter Qwen2.5-Instruct model works well::

       transformers download Qwen/Qwen2.5-1.5B-Instruct
       transformers serve

   The server listens on http://localhost:8000 by default.

Environment variables (all optional)
-------------------------------------
TRANSFORMERS_SERVE_URL : base URL of the running server
    Default: ``http://localhost:8000``
TRANSFORMERS_MODEL : HuggingFace model ID served by the server
    Default: ``Qwen/Qwen2.5-1.5B-Instruct``

Running the tests
-----------------
::

    pytest tests/test_transformers_serve.py -v

The tests are skipped automatically when the server is not reachable.
"""

from __future__ import annotations

import os
import shutil
import tempfile
import urllib.request
from typing import cast
from unittest.mock import patch

import pytest

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SERVE_URL: str = os.environ.get("TRANSFORMERS_SERVE_URL", "http://localhost:8000")
MODEL_ID: str = os.environ.get("TRANSFORMERS_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")
V1_URL: str = f"{SERVE_URL}/v1"

# Environment variables that point langchain's init_chat_model to the local server.
_LANGCHAIN_ENV: dict[str, str] = {
    "LLM_MODEL": MODEL_ID,
    "LLM_PROVIDER": "openai",
    "OPENAI_API_KEY": "fake",
    "OPENAI_BASE_URL": V1_URL,
}


# ---------------------------------------------------------------------------
# Helpers / fixtures
# ---------------------------------------------------------------------------

def _server_reachable() -> bool:
    """Return True when the transformers serve instance responds to /v1/models."""
    try:
        with urllib.request.urlopen(f"{SERVE_URL}/v1/models", timeout=3):
            return True
    except Exception:
        return False


requires_server = pytest.mark.skipif(
    not _server_reachable(),
    reason=(
        "transformers serve is not running. "
        f"Start it with: transformers serve  (expected at {SERVE_URL})"
    ),
)


@pytest.fixture()
def isolated_db(tmp_path):
    """
    Run each DB-touching test in an isolated temporary database so that tests
    never corrupt the real project database and remain idempotent.
    """
    db_dir = tmp_path / "databases"
    db_dir.mkdir()
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    db_path = str(db_dir / "entities.sqlite")

    with (
        patch("app.database.Path") as mock_path,
        patch("app.database.create_engine") as mock_engine,
    ):
        # Redirect the SQLite URL to the temporary file.
        from sqlalchemy import create_engine as real_create_engine

        def _temp_engine(url, **kwargs):
            temp_url = f"sqlite:///{db_path}"
            return real_create_engine(temp_url, **kwargs)

        mock_engine.side_effect = _temp_engine
        mock_path.return_value.exists.return_value = False

        # Reset the cached engine so our patched factory is used.
        import app.database as db_module
        original_engine = db_module._database_engine
        db_module._database_engine = None

        yield tmp_path

        db_module._database_engine = original_engine


# ---------------------------------------------------------------------------
# 1. /v1/chat/completions  –  langchain ChatOpenAI
# ---------------------------------------------------------------------------

@requires_server
def test_chat_completions_via_langchain():
    """
    Verifies the /v1/chat/completions endpoint through langchain's ChatOpenAI
    integration.  This is the primary endpoint used by the gameplay and
    srdparse graphs.
    """
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=MODEL_ID,
        base_url=V1_URL,
        api_key="fake",
        temperature=0.1,
        max_tokens=64,
    )
    response = llm.invoke("Reply with a single word: hello")
    assert response.content, "Expected a non-empty response from /v1/chat/completions"
    print(f"\n[chat/completions] response: {response.content!r}")


@requires_server
def test_chat_completions_streaming_via_langchain():
    """
    Verifies streaming works for /v1/chat/completions via langchain.
    """
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=MODEL_ID,
        base_url=V1_URL,
        api_key="fake",
        temperature=0.1,
        max_tokens=64,
    )
    chunks = list(llm.stream("Count from 1 to 3, one number per line."))
    assert chunks, "Expected at least one streamed chunk"
    full_text = "".join(c.content for c in chunks if c.content)
    assert full_text, "Expected non-empty streamed text"
    print(f"\n[chat/completions streaming] full text: {full_text!r}")


# ---------------------------------------------------------------------------
# 2. /v1/responses  –  openai Responses API
# ---------------------------------------------------------------------------

@requires_server
def test_responses_api_via_openai_client():
    """
    Verifies the /v1/responses endpoint using the official openai Python client.
    The Responses API is OpenAI's latest stateful endpoint; transformers serve
    exposes it experimentally.
    """
    from openai import OpenAI

    client = OpenAI(base_url=V1_URL, api_key="fake")
    response = client.responses.create(
        model=MODEL_ID,
        instructions="You are a helpful assistant.",
        input="Reply with a single word: hello",
        max_output_tokens=32,
    )
    assert response.output, "Expected at least one output item from /v1/responses"
    text = response.output[0].content[0].text
    assert text, "Expected non-empty text in /v1/responses output"
    print(f"\n[responses] text: {text!r}")


@requires_server
def test_responses_api_streaming_via_openai_client():
    """
    Verifies the streaming variant of /v1/responses.
    """
    from openai import OpenAI

    client = OpenAI(base_url=V1_URL, api_key="fake")
    chunks = []
    for event in client.responses.create(
        model=MODEL_ID,
        input="Count from 1 to 3, one number per line.",
        max_output_tokens=64,
        stream=True,
    ):
        chunks.append(event)
    assert chunks, "Expected at least one SSE event from /v1/responses stream"
    print(f"\n[responses streaming] received {len(chunks)} events")


# ---------------------------------------------------------------------------
# 3. srdparse graph  –  database building
# ---------------------------------------------------------------------------

@requires_server
def test_srdparse_graph_builds(isolated_db):
    """
    Verifies that build_graph() from app.graph.srdparse compiles successfully
    and that the graph can be invoked against the real SRD source file.

    The srd_splitter node is pure Python (no LLM call); the parser nodes use
    structured output via the configured LLM.  Under transformers serve the
    full parse run may take a long time, so this test only checks that the
    graph compiles and that the initial splitting step succeeds.
    """
    with patch.dict(os.environ, _LANGCHAIN_ENV):
        from app.graph.srdparse import build_graph
        from app.database import initialize_database
        from app.types.state import SrdParserState

        graph = build_graph()
        assert graph is not None, "srdparse graph failed to compile"

        initialize_database()

        # Run only the srd_splitter step by invoking the graph with the real
        # SRD source file and catching any LLM errors so that the test reports
        # a clear assertion rather than an unrelated network/model failure.
        try:
            result = graph.invoke(cast(SrdParserState, {"source_file": "SRD_CC_v5.2.1.md"}))
            sections: list[str] = result.get("sections", [])
            assert sections, "srd_splitter produced no sections from the SRD file"
            assert "Equipment" in sections, "Expected 'Equipment' section in SRD parse result"
            print(f"\n[srdparse] split into {len(sections)} sections: {sections[:5]} …")
        except Exception as exc:
            pytest.fail(
                f"srdparse graph invocation failed: {exc}\n"
                "Make sure the model supports structured output / function calling."
            )


# ---------------------------------------------------------------------------
# 4. gameplay graph  –  tool use
# ---------------------------------------------------------------------------

@requires_server
def test_gameplay_graph_with_tools(isolated_db):
    """
    Verifies that build_graph() from app.graph.gameplay compiles and that the
    graph can process a user message using the player tools.

    The gameplay graph uses create_agent (tool calling) in the send_message
    node and structured output in the planner node.  Both require a model that
    supports tool / function calling.
    """
    with patch.dict(os.environ, _LANGCHAIN_ENV):
        from app.graph.gameplay import build_graph
        from app.database import initialize_database
        from app.test import create_random_player
        from app.prompts import CAMPAIGN_PROMPT
        from app.types.state import GameplayState
        from langchain.messages import HumanMessage

        initialize_database()

        graph = build_graph()
        assert graph is not None, "gameplay graph failed to compile"

        player = create_random_player(persist=False)
        state: GameplayState = {
            "messages": [
                HumanMessage(content=CAMPAIGN_PROMPT),
                HumanMessage(content="Guarda intorno e dimmi cosa vedi."),
            ],
            "player": player,
            "plan": None,
        }

        try:
            result = cast(GameplayState, graph.invoke(state))
            messages = result.get("messages", [])
            assert messages, "gameplay graph returned no messages"
            last_msg = messages[-1]
            assert last_msg.content, "Last message from gameplay graph is empty"
            print(f"\n[gameplay] last message: {last_msg.content[:200]!r} …")
        except Exception as exc:
            pytest.fail(
                f"gameplay graph invocation failed: {exc}\n"
                "Make sure the model supports tool / function calling."
            )
