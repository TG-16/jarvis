from ollama import chat

class OllamaClient:
    def __init__(self, model):
        self.model = model

    def stream_chat(self, messages):
        stream = chat(
            model=self.model,
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            yield chunk["message"]["content"]