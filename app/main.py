from automation.browser_manager import BrowserManager


def main():
    browser = BrowserManager()

    browser.open("https://quotes.toscrape.com")

    print(browser.get_title())

    browser.wait(2000)

    browser.click("text=Next →")

    browser.wait(3000)

    browser.take_screenshot("second_page.png")

    browser.close()


if __name__ == "__main__":
    main()