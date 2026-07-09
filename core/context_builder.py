class ContextBuilder:
    """
    Builds the context that is sent to the LLM.
    """

    def __init__(
        self,
        system_prompt,
        conversation_manager,
        memory_store,
    ):
        self.system_prompt = system_prompt
        self.conversation_manager = conversation_manager
        self.memory_store = memory_store

    def build(self, user_message):
        """
        Build the complete conversation context.
        """

        long_term_memory = self.memory_store.load()

        system_prompt = (
            f"{self.system_prompt}\n\n"
            "-----------------------------\n"
            "Long-Term Memory\n"
            "-----------------------------\n"
            f"{long_term_memory}"
        )

        messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        messages.extend(
            self.conversation_manager.get_recent_messages()
        )

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        return messages