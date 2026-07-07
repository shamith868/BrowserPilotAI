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
        print("Links:", self.page.locator("a").count())
        print("Buttons:", self.page.locator("button").count())
        print("Inputs:", self.page.locator("input").count())

        print("\n========== FIRST 15 HEADINGS ==========\n")

        headings = self.page.locator("h1, h2, h3")

        count = min(15, headings.count())

        for i in range(count):

            try:
                print(f"{i+1}. {headings.nth(i).inner_text()}")

            except Exception:
                pass

        print("\n========== FIRST 10 ARTICLES ==========\n")

        articles = self.page.locator("article")

        print("Articles found:", articles.count())

        for i in range(min(10, articles.count())):

            print("\n------------------------------")

            try:
                print(articles.nth(i).inner_text()[:500])

            except Exception:
                pass

        self.page.wait_for_timeout(30000)

        self.browser.close()
        self.playwright.stop()


if __name__ == "__main__":

    explorer = SelectorExplorer()

    explorer.explore("https://github.com/search?q=playwright&type=repositories")