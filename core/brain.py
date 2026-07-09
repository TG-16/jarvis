from config.settings import SYSTEM_PROMPT_PATH
from core.prompt_loader import PromptLoader
from core.context_builder import ContextBuilder


class Brain:
    """
    Coordinates the assistant's reasoning.
    """

    def __init__(
        self,
        llm_client,
        conversation_manager,
        memory_store,
    ):
        self.llm = llm_client

        self.system_prompt = PromptLoader.load(
            SYSTEM_PROMPT_PATH
        )

        self.context_builder = ContextBuilder(
            self.system_prompt,
            conversation_manager,
            memory_store,
        )

    def think(self, user_message):
        """
        Build context and stream the response.
        """

        messages = self.context_builder.build(
            user_message
        )

        return self.llm.stream_chat(messages)