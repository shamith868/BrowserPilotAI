from automation.browser_manager import BrowserManager

browser = BrowserManager()

browser.open("https://github.com/search?q=selenium&type=repositories")

browser.wait(5000)

card = browser.get_elements('[data-testid="results-list"] > div').first

print("\nRepository Name:")
print(card.locator("h3 a").inner_text())

print("\nDescription:")
print(card.locator(".Content-module__Content__mHmep").inner_text())

print("\nLanguage:")
print(card.locator('[aria-label$="language"]').inner_text())

print("\nStars:")
print(card.locator('[href$="/stargazers"] span').last.inner_text())

print("\nURL:")
print(card.locator("h3 a").get_attribute("href"))

browser.close()