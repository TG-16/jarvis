from pathlib import Path

SYSTEM_NAME = "Jarvis"

MODEL_NAME = "qwen2.5-coder:7b"

BASE_DIR = Path(__file__).resolve().parent.parent

SYSTEM_PROMPT_PATH = BASE_DIR / "prompts" / "system_prompt.txt"

CONVERSATION_FILE = BASE_DIR / "memory" / "conversations.json"

MEMORY_FILE = BASE_DIR / "memory" / "memory.md"