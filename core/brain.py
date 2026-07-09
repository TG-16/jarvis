class Brain:
    def __init__(self, llm_client):
        self.llm = llm_client

    def think(self, user_message):
        """
        Processes the user's message and returns a response.

        In future versions this method will:
        - Read long-term memory
        - Retrieve recent conversations
        - Search the Obsidian vault
        - Call tools
        - Build the final prompt

        For now, it simply forwards the message to the LLM.
        """
        return self.llm.chat(user_message)