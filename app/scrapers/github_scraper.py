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

        print(f"Searching GitHub for: {keyword}")

        self.browser.open(url)

        self.browser.wait(5000)

        links = self.browser.get_elements("a")

        os.makedirs("data", exist_ok=True)

        with open(
            "data/github_repositories.csv",
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(["Repository", "URL"])

            added = set()

            for i in range(links.count()):

                try:

                    text = links.nth(i).inner_text().strip()

                    href = links.nth(i).get_attribute("href")

                    if (
                        href
                        and href.count("/") == 2
                        and not href.startswith("/topics")
                        and not href.endswith("/stargazers")
                        and text
                    ):

                        full_url = "https://github.com" + href

                        if full_url not in added:

                            added.add(full_url)

                            writer.writerow([text, full_url])

                            print(text)

                except Exception:
                    pass

        print(f"\nSaved {len(added)} repositories.")

        self.browser.close()