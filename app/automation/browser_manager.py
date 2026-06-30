import os
from playwright.sync_api import sync_playwright


class BrowserManager:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open(self, url):
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

    def close(self):
        self.browser.close()
        self.playwright.stop()