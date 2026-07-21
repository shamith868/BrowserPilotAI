from automation.browser_manager import BrowserManager

browser = BrowserManager()

browser.open("https://github.com/microsoft/playwright")

browser.wait(5000)

selectors = [
    "article",
    "#readme",
    "#readme article",
    "article.markdown-body",
    ".markdown-body",
    "[data-testid='readme']"
]

for selector in selectors:

    print("\n==============================")
    print("Checking:", selector)

    if browser.exists(selector):

        print("Found!")

        try:

            text = browser.read_text(selector)

            print(text[:1000])

        except Exception as e:

            print("Couldn't read:", e)

    else:

        print("Not Found")

browser.close()