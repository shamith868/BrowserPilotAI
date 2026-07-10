import json
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

        content = response["message"]["content"]

        # Remove markdown if Gemma returns ```json ... ```
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        return content

    def ask_json(self, prompt):

        response = self.ask(prompt)

        return json.loads(response)