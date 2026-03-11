from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class BaseButtonPage(BasePage):

    def __init__(self, page: Page, button_locator: str) -> None:
        super().__init__(page)
        self.button = page.locator(button_locator)
        self.result = page.locator("#result-text")

    def click(self):
        self.button.click()

    def should_have_button_labeled(self, label: str) -> None:
        expect(self.button).to_have_text(label)

    def should_have_result_text(self, text: str) -> None:
        expect(self.result).to_have_text(text)
