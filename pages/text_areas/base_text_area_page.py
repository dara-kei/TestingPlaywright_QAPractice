from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class BaseTextAreaPage(BasePage):
    def __init__(self, page, error_locator: str):
        super().__init__(page)
        self.button = page.locator("#submit-id-submit")
        self.result = page.locator("#result-text")
        self.error = page.locator(error_locator)


    @allure.step("Click submit button")
    def submit(self):
        self.button.click()


    @allure.step("Check result text is {expected}")
    def should_have_result_text(self, expected):
        expect(self.result).to_have_text(expected)


    @allure.step("Check result text is not displayed")
    def should_not_have_result(self):
        expect(self.result).to_have_count(0)


    @allure.step("Check the area is required")
    def should_have_required_area(self, text_area):
        expect(text_area).to_have_attribute("required", "")


    @allure.step("Check error message is displayed")
    def should_have_error_message(self, error_message):
        expect(self.error).to_have_text(error_message)

