from config.settings import MODEL_NAME, CONVERSATION_FILE

from llm.ollama_client import OllamaClient
from memory.conversation_manager import ConversationManager
from core.brain import Brain
from core.assistant import Assistant


def main():
    llm_client = OllamaClient(MODEL_NAME)

    conversation_manager = ConversationManager(CONVERSATION_FILE)

    brain = Brain(
        llm_client,
        conversation_manager,
    )

    assistant = Assistant(
        brain,
        conversation_manager,
    )

    assistant.start()


if __name__ == "__main__":
    main()