from playwright.sync_api import sync_playwright


class SelectorExplorer:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def explore(self, url):

        self.page.goto(url)

        self.page.wait_for_timeout(5000)

        print("\n========== PAGE INFORMATION ==========\n")

        print("Title:", self.page.title())
        print("Total Links:", self.page.locator("a").count())
        print("Total Buttons:", self.page.locator("button").count())
        print("Total Inputs:", self.page.locator("input").count())
        print("Total Headings:", self.page.locator("h1, h2, h3, h4, h5").count())

        keyword = input("\nEnter keyword to search inside links: ").lower()

        print("\n========== MATCHES ==========\n")

        links = self.page.locator("a")

        found = 0

        for i in range(links.count()):

            try:
                text = links.nth(i).inner_text().strip()
                href = links.nth(i).get_attribute("href")

                if keyword in text.lower() or (href and keyword in href.lower()):

                    found += 1

                    print(f"{found}. {text}")
                    print(f"   {href}\n")

            except Exception:
                pass

        if found == 0:
            print("No matches found.")

        self.page.wait_for_timeout(30000)

        self.browser.close()

        self.playwright.stop()


if __name__ == "__main__":

    explorer = SelectorExplorer()

    explorer.explore("https://github.com/search?q=playwright&type=repositories")