from automation.browser_manager import BrowserManager
from urllib.parse import quote
import csv
import os


class GitHubScraper:

    def __init__(self):
        self.browser = BrowserManager()

    def scrape(self, keyword):

        encoded_keyword = quote(keyword)

        url = f"https://github.com/search?q={encoded_keyword}&type=repositories"

        print(f"\nSearching GitHub for: {keyword}")

        self.browser.open(url)

        self.browser.wait(5000)

        cards = self.browser.get_elements(
            '[data-testid="results-list"] > div'
        )

        print("\n========== DEBUG ==========")
        print("Keyword      :", keyword)
        print("Current URL  :", self.browser.page.url)
        print("Page Title   :", self.browser.get_title())
        print("Cards Found  :", cards.count())
        print("===========================\n")

        os.makedirs("data", exist_ok=True)

        repositories = []

        with open(
            "data/github_repositories.csv",
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Repository",
                "Description",
                "Language",
                "Stars",
                "URL"
            ])

            for i in range(cards.count()):

                card = cards.nth(i)

                try:

                    name = card.locator("h3 a").inner_text()

                    description = card.locator(
                        ".Content-module__Content__mHmep"
                    ).inner_text()

                    language = card.locator(
                        '[aria-label$="language"]'
                    ).inner_text()

                    stars = card.locator(
                        '[href$="/stargazers"] span'
                    ).last.inner_text()

                    repo_url = (
                        "https://github.com"
                        + card.locator("h3 a").get_attribute("href")
                    )

                except Exception as e:
                    print(f"Skipped card {i}: {e}")
                    continue

                writer.writerow([
                    name,
                    description,
                    language,
                    stars,
                    repo_url
                ])

                repositories.append({
                    "name": name,
                    "description": description,
                    "language": language,
                    "stars": stars,
                    "url": repo_url
                })

                print(f"\n{name}")
                print(description)
                print(language)
                print(stars)

        print(f"\nSaved {len(repositories)} repositories.")

        return repositories

    def close(self):

        self.browser.close()