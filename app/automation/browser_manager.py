import os
from playwright.sync_api import sync_playwright
from utils.logger import logger


class BrowserManager:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open(self, url):
        logger.info(f"Opening {url}")
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def take_screenshot(self, filename):
        os.makedirs("screenshots", exist_ok=True)
        path = os.path.join("screenshots", filename)
        self.page.screenshot(path=path)

    def wait(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

    def click(self, selector):
        self.page.click(selector)
    
    def type(self, selector, text):
        self.page.fill(selector, text)

    def press(self, key):
        self.page.keyboard.press(key)

    def close(self):
        logger.info("Closing browser")
        self.browser.close()
        self.playwright.stop()

    def read_text(self, selector):
        return self.page.locator(selector).inner_text()
    
    def get_elements(self, selector):
        return self.page.locator(selector)
    
    def exists(self, selector):
        return self.page.locator(selector).count() > 0