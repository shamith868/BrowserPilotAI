from llm.ollama_client import OllamaClient
from scrapers.github_scraper import GitHubScraper
from scrapers.quotes_scraper import QuotesScraper


class AIAgent:

    def __init__(self):
        self.ai = OllamaClient()

    def run(self, command):

        prompt = f"""
You are an AI assistant.

Available tools:
- github
- quotes

Return ONLY valid JSON.

Examples:

{{
    "tool": "github",
    "keyword": "playwright"
}}

{{
    "tool": "quotes",
    "keyword": ""
}}

User request:
{command}
"""

        decision = self.ai.ask_json(prompt)

        print("\nAI Decision:", decision)

        tool = decision["tool"].lower()
        keyword = decision["keyword"]

        if tool == "github":

            scraper = GitHubScraper()
            scraper.scrape(keyword)

        elif tool == "quotes":

            scraper = QuotesScraper()
            scraper.scrape()

        else:

            print("Unknown tool:", tool)