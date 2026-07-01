import csv
from utils.logger import logger
from config import BASE_URL, WAIT_TIME, OUTPUT_FILE


class QuotesScraper:

    def __init__(self, browser):
        self.browser = browser

    def scrape(self):

        self.browser.open(BASE_URL)

        self.browser.wait(WAIT_TIME)

        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(["Quote", "Author"])

            page_number = 1

            while True:

                logger.info(f"Scraping Page {page_number}")

                quotes = self.browser.get_elements(".quote")

                count = quotes.count()

                for i in range(count):

                    quote = quotes.nth(i).locator(".text").inner_text()

                    author = quotes.nth(i).locator(".author").inner_text()

                    writer.writerow([quote, author])

                logger.info(f"Processed {count} quotes from page {page_number}")

                if self.browser.exists(".next"):

                    self.browser.click(".next a")

                    self.browser.wait(WAIT_TIME)

                    page_number += 1

                else:

                    break

        logger.info("Finished scraping all pages.")