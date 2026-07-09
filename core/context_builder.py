class ContextBuilder:
    """
    Builds the context sent to the LLM.
    """

    def __init__(self, system_prompt, conversation_manager):
        self.system_prompt = system_prompt
        self.conversation_manager = conversation_manager

    def build(self, user_message):
        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
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