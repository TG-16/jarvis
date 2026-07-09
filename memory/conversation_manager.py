import json
from pathlib import Path


class ConversationManager:
    """
    Manages the conversation history.

    Responsibilities:
    - Load conversations from disk
    - Save conversations
    - Add new messages
    - Return recent conversation history
    """

    def __init__(self, file_path, max_messages=20):
        self.file_path = Path(file_path)
        self.max_messages = max_messages

        self.messages = self._load()

    def _load(self):
        if not self.file_path.exists():
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return []

    def _save(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.messages, file, indent=4)

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

        self._trim()
        self._save()

    def add_assistant_message(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })

        self._trim()
        self._save()

    def get_recent_messages(self):
        return self.messages

    def _trim(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]