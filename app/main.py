from automation.browser_manager import BrowserManager


def main():
    browser = BrowserManager()

    browser.open("https://www.google.com")

    browser.wait(2000)

    browser.type('textarea[name="q"]', "Playwright Python Tutorial")

    browser.wait(1000)

    browser.press("Enter")

    browser.wait(3000)

    browser.take_screenshot("google_results.png")

    browser.close()


if __name__ == "__main__":
    main()