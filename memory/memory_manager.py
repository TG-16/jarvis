from memory.memory_extractor import MemoryExtractor


class MemoryManager:
    """
    Coordinates long-term memory updates.

    Responsibilities:
    - Decide whether new information should be remembered.
    - Update memory.md when appropriate.
    """

    def __init__(self, llm_client, memory_store):
        self.llm = llm_client
        self.memory_store = memory_store
        self.extractor = MemoryExtractor(llm_client)

    def process(self, user_message):
        """
        Process a user message and update memory if needed.
        """

        decision = self.extractor.extract(user_message)

        if not decision.get("remember"):
            return

        existing_memory = self.memory_store.load()

        prompt = f"""
You maintain the long-term memory of an AI assistant.

Existing Memory:

{existing_memory}

----------------------------------------

New Fact:

{decision["fact"]}

----------------------------------------

Instructions:

- Merge the new fact into the existing memory.
- Keep the markdown structure.
- Do not duplicate information.
- Update existing fields if necessary.
- Preserve all unrelated information.
- Return ONLY the updated markdown.
"""

        updated_memory = self.llm.generate(prompt)

        self.memory_store.save(updated_memory)