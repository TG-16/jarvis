from config.settings import MODEL_NAME
from llm.ollama_client import OllamaClient
from memory.memory_extractor import MemoryExtractor


llm = OllamaClient(MODEL_NAME)

extractor = MemoryExtractor(llm)

while True:
    text = input("Message: ")

    result = extractor.extract(text)

    print(result)