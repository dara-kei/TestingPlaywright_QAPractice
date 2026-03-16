from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class BaseCheckboxPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button = page.locator("#submit-id-submit")
        self.result = page.locator("#result-text")

    def submit(self):
        self.button.click()

    def should_have_button_named(self, text):
        expect(self.button).to_have_value(text)

    def should_have_button_enabled(self):
        expect(self.button).to_be_enabled()

    def should_have_result_text(self, text):
        expect(self.result).to_have_text(text)

    def should_not_have_result(self):
        expect(self.result).to_have_count(0)