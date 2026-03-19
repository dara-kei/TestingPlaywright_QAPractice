from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure

class BaseCheckboxPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button = page.locator("#submit-id-submit")
        self.result = page.locator("#result-text")

    @allure.step("Click the button to submit checkbox")
    def submit(self):
        self.button.click()

    @allure.step("Check the button name")
    def should_have_button_named(self, text):
        expect(self.button).to_have_value(text)

    @allure.step("Check the button is enabled")
    def should_have_button_enabled(self):
        expect(self.button).to_be_enabled()

    @allure.step("Check the result text is {text}")
    def should_have_result_text(self, text):
        expect(self.result).to_have_text(text)

    @allure.step("Check result is not displayed")
    def should_not_have_result(self):
        expect(self.result).to_have_count(0)