import ollama


class OllamaClient:

    def __init__(self, model="gemma3:4b"):
        self.model = model

    def ask(self, prompt):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]