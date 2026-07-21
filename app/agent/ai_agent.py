from llm.ollama_client import OllamaClient
from scrapers.quotes_scraper import QuotesScraper
from services.github_service import GitHubService


class AIAgent:

    def __init__(self):

        self.ai = OllamaClient()
        self.github = GitHubService()

    def run(self, command):

        prompt = f"""
You are BrowserPilotAI.

Your job is to understand the user's request and decide which tool should be used.

Available tools:

1. github
   - Searches ONE GitHub repository.
   - keyword should contain only one technology.

2. compare
   - Compare TWO technologies.
   - Return:
        first_keyword
        second_keyword

3. quotes
   - Returns a motivational quote.

Return ONLY valid JSON.

Examples:

User:
Find Playwright repositories on GitHub

Output:
{{
    "tool":"github",
    "keyword":"playwright"
}}

User:
Compare Playwright and Selenium

Output:
{{
    "tool":"compare",
    "first_keyword":"playwright",
    "second_keyword":"selenium"
}}

User:
Compare React with Vue

Output:
{{
    "tool":"compare",
    "first_keyword":"react",
    "second_keyword":"vue"
}}

User:
Give me a motivational quote

Output:
{{
    "tool":"quotes"
}}

User Request:
{command}
"""

        decision = self.ai.ask_json(prompt)

        print("\n========== AI DECISION ==========")
        print(decision)
        print("================================\n")

        tool = decision["tool"].lower()

        if tool == "github":

            self.github.search(
                decision["keyword"]
            )

        elif tool == "compare":

            print("\nSearching for first technology...\n")

            self.github.search(
                decision["first_keyword"]
            )

            print("\nSearching for second technology...\n")

            self.github.search(
                decision["second_keyword"]
            )

        elif tool == "quotes":

            scraper = QuotesScraper()
            scraper.scrape()

        else:

            print("Unknown tool:", tool)