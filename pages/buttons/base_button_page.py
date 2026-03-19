from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

class BaseButtonPage(BasePage):

    def __init__(self, page: Page, button_locator: str) -> None:
        super().__init__(page)
        self.button = page.locator(button_locator)
        self.result = page.locator("#result-text")

    @allure.step("Click the button")
    def click(self):
        self.button.click()

    @allure.step("Check the button name")
    def should_have_button_labeled(self, label: str) -> None:
        expect(self.button).to_have_text(label)

    @allure.step("Check the result text is {text}")
    def should_have_result_text(self, text: str) -> None:
        expect(self.result).to_have_text(text)
