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

        return response["message"]["content"]

    def ask_json(self, prompt):

        response = self.ask(prompt)

        start = response.find("{")
        end = response.rfind("}") + 1

        json_text = response[start:end]

        return json.loads(json_text)

    def summarize_repositories(self, keyword, repositories):

        count = len(repositories)

        repo_text = ""

        for repo in repositories:

            repo_text += f"""
Repository: {repo['name']}
Description: {repo['description']}
Language: {repo['language']}
Stars: {repo['stars']}
URL: {repo['url']}

"""

        prompt = f"""
You are BrowserPilotAI.

The browser automation has already completed successfully.

Search keyword:
{keyword}

Exact repository count:
{count}

Repository Details:

{repo_text}

Write a professional summary.

Rules:

1. Use the EXACT repository count.
2. Do NOT invent numbers.
3. Mention the search keyword.
4. Mention the most popular repositories based on their star counts.
5. Mention interesting programming languages if relevant.
6. Mention that the repository information has been saved to a CSV file.
7. Keep the summary under 120 words.
"""

        return self.ask(prompt)

    def explain_repository(self, repository_name, readme):

        prompt = f"""
You are BrowserPilotAI.

Repository:
{repository_name}

README:

{readme[:12000]}

Explain this repository in simple English.

Your answer should include:

1. What is this project?
2. What problem does it solve?
3. Main features.
4. Who should use it?
5. Keep the explanation under 200 words.
"""

        return self.ask(prompt)

    def compare_repositories(
        self,
        first_name,
        first_readme,
        second_name,
        second_readme
    ):

        prompt = f"""
You are BrowserPilotAI.

Compare these two GitHub projects.

Repository 1:
{first_name}

README:
{first_readme[:10000]}


Repository 2:
{second_name}

README:
{second_readme[:10000]}

Write a comparison.

Include:

1. What each project is.
2. Main differences.
3. Advantages of each.
4. When to choose each.
5. Final recommendation.

Keep it under 300 words.
"""

        return self.ask(prompt)