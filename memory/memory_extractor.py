class MemoryExtractor:
    """
    Uses the LLM to determine whether a user message
    should become long-term memory.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def extract(self, user_message):
        """
        Returns:

        {
            "remember": bool,
            "reason": "...",
            "fact": "..."
        }
        """

        messages = [
            {
                "role": "system",
                "content": """
You are a memory classifier.

Your task is to determine whether the latest user message
contains useful long-term information.

Remember ONLY:

- Name
- Preferences
- Skills
- Goals
- Projects
- Long-term plans
- Personal facts explicitly requested to remember

Do NOT remember:

- Greetings
- Questions
- Temporary events
- Casual conversation
- One-time activities

Return ONLY valid JSON.

Required format:

{
    "remember": true,
    "reason": "...",
    "fact": "..."
}
"""
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        result = self.llm.chat_json(messages)

        if result is None:
            return {
                "remember": False,
                "reason": "Invalid JSON returned.",
                "fact": ""
            }

        return result