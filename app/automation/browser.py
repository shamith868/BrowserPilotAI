from playwright.sync_api import sync_playwright


def open_browser():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto("https://quotes.toscrape.com")

        print(f"Title : {page.title()}")
        print(f"URL   : {page.url}")

        page.wait_for_selector(".quote")

        quotes = page.locator(".quote")

        count = quotes.count()

        print(f"\nFound {count} quotes\n")

        for i in range(count):

            quote = quotes.nth(i).locator(".text").inner_text()

            author = quotes.nth(i).locator(".author").inner_text()

            print(f"{i+1}. {quote}")
            print(f"   - {author}\n")

        page.wait_for_timeout(10000)

        browser.close()


if __name__ == "__main__":
    open_browser()