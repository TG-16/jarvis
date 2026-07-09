import json
from ollama import chat, generate, embed


class OllamaClient:
    """
    Wrapper around the Ollama Python SDK.

    Responsibilities:
    - Stream conversations
    - Standard chat requests
    - Structured JSON responses
    - Text generation
    - Embedding generation
    """

    def __init__(self, model):
        self.model = model

    def stream_chat(self, messages):
        """
        Stream a response token-by-token.
        Used for normal conversations.
        """

        stream = chat(
            model=self.model,
            messages=messages,
            stream=True,
        )

        for chunk in stream:
            yield chunk["message"]["content"]

    def chat(self, messages):
        """
        Standard non-streaming chat.
        Returns plain text.
        """

        response = chat(
            model=self.model,
            messages=messages,
            stream=False,
        )

        return response["message"]["content"]

    def chat_json(self, messages):
        """
        Ask Ollama to return JSON only.
        """

        response = chat(
            model=self.model,
            messages=messages,
            stream=False,
            format="json",
        )

        content = response["message"]["content"]

        try:
            return json.loads(content)

        except json.JSONDecodeError:
            print("\n========== INVALID JSON ==========")
            print(content)
            print("==================================\n")

            return None

    def generate(self, prompt):
        """
        Generate text from a prompt.
        """

        response = generate(
            model=self.model,
            prompt=prompt,
        )

        return response["response"]

    def embeddings(self, text):
        """
        Generate embeddings.
        """

        response = embed(
            model=self.model,
            input=text,
        )

        return response["embeddings"][0]