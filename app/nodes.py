from app.state import State
from langchain.chat_models import init_chat_model

def send_message(state: State):
	chat_model = init_chat_model(model='qwen/qwen3.5-397b-a17b', model_provider='nvidia')
	response = chat_model.invoke(state['messages'])
	return {'messages': [response]}