from app.types.state import State
from app.tools import tools_list
from langchain.chat_models import init_chat_model

def send_message(state: State) -> dict:
	chat_model = init_chat_model(model='qwen3.5:397b-cloud', model_provider='ollama').bind_tools(tools_list)
	response = chat_model.invoke(state['messages'])
	return {'messages': [response]}