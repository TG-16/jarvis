from pathlib import Path

MODEL_NAME = "qwen2.5-coder:7b"

SYSTEM_NAME = "Jarvis"

BASE_DIR = Path(__file__).resolve().parent.parent

SYSTEM_PROMPT_PATH = BASE_DIR / "prompts" / "system_prompt.txt"

CONVERSATION_FILE = BASE_DIR / "memory" / "conversations.json"