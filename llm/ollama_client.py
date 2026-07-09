from ollama import chat


class OllamaClient:
    def __init__(self, model):
        self.model = model

    def chat(self, message):
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]