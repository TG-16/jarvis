from config.settings import MODEL_NAME

from llm.ollama_client import OllamaClient
from core.brain import Brain
from core.assistant import Assistant


def main():
    llm_client = OllamaClient(MODEL_NAME)

    brain = Brain(llm_client)

    assistant = Assistant(brain)

    assistant.start()


if __name__ == "__main__":
    main()