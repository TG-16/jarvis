from config.settings import (
    MODEL_NAME,
    CONVERSATION_FILE,
    MEMORY_FILE,
)

from llm.ollama_client import OllamaClient

from memory.conversation_manager import ConversationManager
from memory.memory_store import MemoryStore
from memory.memory_manager import MemoryManager

from core.brain import Brain
from core.assistant import Assistant


def main():
    llm_client = OllamaClient(MODEL_NAME)

    conversation_manager = ConversationManager(CONVERSATION_FILE)

    memory_store = MemoryStore(MEMORY_FILE)

    memory_manager = MemoryManager(
        llm_client,
        memory_store,
    )

    brain = Brain(
        llm_client,
        conversation_manager,
        memory_store,
    )

    assistant = Assistant(
        brain,
        conversation_manager,
        memory_manager,
    )

    assistant.start()


if __name__ == "__main__":
    main()