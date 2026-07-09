from config.settings import SYSTEM_PROMPT_PATH
from core.prompt_loader import PromptLoader
from core.context_builder import ContextBuilder


class Brain:
    """
    Coordinates the assistant's reasoning.
    """

    def __init__(self, llm_client, conversation_manager):
        self.llm = llm_client

        self.system_prompt = PromptLoader.load(SYSTEM_PROMPT_PATH)

        self.context_builder = ContextBuilder(
            self.system_prompt,
            conversation_manager,
        )

    def think(self, user_message):
        messages = self.context_builder.build(user_message)

        return self.llm.stream_chat(messages)