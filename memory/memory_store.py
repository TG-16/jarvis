from pathlib import Path


class MemoryStore:
    """
    Handles reading and writing the long-term memory file.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):
        """
        Load the contents of memory.md.
        """

        if not self.file_path.exists():
            return ""

        return self.file_path.read_text(
            encoding="utf-8"
        )

    def save(self, content):
        """
        Save content to memory.md.
        """

        self.file_path.write_text(
            content,
            encoding="utf-8"
        )