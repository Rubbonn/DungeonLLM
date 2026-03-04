if __name__ == "__main__":
    import dotenv
    from langchain.chat_models import init_chat_model

    dotenv.load_dotenv()
    chat_model = init_chat_model(model='qwen/qwen3.5-397b-a17b', model_provider='nvidia')

    response = chat_model.invoke('Ciao come stai?')
    print(response.content)