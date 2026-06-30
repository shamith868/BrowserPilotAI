from automation.browser_manager import BrowserManager


def main():
    browser = BrowserManager()

    browser.open("https://quotes.toscrape.com")

    print(browser.get_title())

    browser.take_screenshot("homepage.png")
    print("Screenshot saved successfully!")

    # Using the clean custom wait method now
    browser.wait(5000)

    browser.close()


if __name__ == "__main__":
    main()