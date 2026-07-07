from scrapers.github_scraper import GitHubScraper
from scrapers.quotes_scraper import QuotesScraper


class AIAgent:

    def run(self, command):

        command = command.lower()

        if "github" in command or "repository" in command:

            keyword = command

            keyword = keyword.replace("github", "")
            keyword = keyword.replace("repositories", "")
            keyword = keyword.replace("repository", "")
            keyword = keyword.strip()

            if keyword == "":
                keyword = "python"

            scraper = GitHubScraper()
            scraper.scrape(keyword)

        elif "quote" in command:

            scraper = QuotesScraper()
            scraper.scrape()

        else:

            print("Sorry, I don't know how to do that yet.")