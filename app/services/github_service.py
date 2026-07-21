from tools.github_tools import GitHubTools
from llm.ollama_client import OllamaClient


class GitHubService:

    def __init__(self):

        self.github = GitHubTools()
        self.ai = OllamaClient()

    def search(self, keyword):

        data = self.github.get_repository_information(keyword)

        if data is None:

            print("No repositories found.")
            self.github.close()
            return

        repositories = data["repositories"]
        repository = data["repository"]
        readme = data["readme"]

        summary = self.ai.summarize_repositories(
            keyword,
            repositories
        )

        print("\n========== SEARCH SUMMARY ==========\n")
        print(summary)

        if readme:

            explanation = self.ai.explain_repository(
                repository["name"],
                readme
            )

            print("\n========== REPOSITORY EXPLANATION ==========\n")
            print(explanation)

        self.github.close()