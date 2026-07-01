from automation.browser_manager import BrowserManager
from scrapers.quotes_scraper import QuotesScraper


class BrowserAgent:

    def __init__(self):
        self.browser = BrowserManager()

    def scrape_quotes(self):
        scraper = QuotesScraper(self.browser)
        scraper.scrape()

    def close(self):
        self.browser.close()