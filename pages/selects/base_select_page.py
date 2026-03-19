from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class BaseSelectPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.submit_btn_locator = page.locator("#submit-id-submit")
        self.result_text_locator = page.locator("#result-text")


    @allure.step("Click submit button")
    def submit(self) -> None:
        self.submit_btn_locator.click()


    @allure.step("Check result text is {expected_result}")
    def should_have_result_text(self, expected_result) -> None:
        expect(self.result_text_locator).to_have_text(expected_result)


    @allure.step("Check result is not displayed")
    def should_not_have_result(self) -> None:
        expect(self.result_text_locator).to_have_count(0)
