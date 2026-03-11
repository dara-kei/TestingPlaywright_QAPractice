from playwright.sync_api import Page, expect


class BasePage:
    URL = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if not self.URL:
            raise NotImplementedError("Page URL is not defined")
        self.page.goto(self.URL)

