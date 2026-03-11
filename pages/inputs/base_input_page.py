from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class InputBasePage(BasePage):

    def __init__(self, page: Page, text_input_locator: str, error_locator: str) -> None:
        super().__init__(page)
        self.text_input = page.locator(text_input_locator)
        self.result = page.locator("#result-text")
        self.error = page.locator(error_locator)


    def enter_text_input_and_submit(self, text) -> None:
        self.text_input.fill(text)
        self.text_input.press("Enter")

    def result_text_should_be_visible(self)-> None:
        expect(self.result).to_be_visible()

    def should_have_result_text(self, text) -> None:
        expect(self.result).to_have_text(text)

    def validation_message(self)-> str:
        return self.text_input.evaluate("el => el.validationMessage")

    def check_text_field_is_required(self)-> None:
        expect(self.text_input).to_have_attribute("required", "")

    def should_have_error_message(self, text) -> None:
        expect(self.error).to_have_text(text)

