from playwright.sync_api import Page, expect
import allure

class BasePage:
    URL = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open testing page")
    def open(self):
        if not self.URL:
            raise NotImplementedError("Page URL is not defined")
        self.page.goto(self.URL)

