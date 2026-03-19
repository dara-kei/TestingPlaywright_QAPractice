from playwright.sync_api import Page, expect
from pages.buttons.base_button_page import BaseButtonPage
import allure


class DisabledButtonPage(BaseButtonPage):
    URL = "https://www.qa-practice.com/elements/button/disabled"

    def __init__(self, page: Page) -> None:
        super().__init__(page, "#submit-id-submit")
        self.select = page.locator("#id_select_state")

    @allure.step("Check the button is disabled")
    def should_have_disabled_button(self):
        expect(self.button).to_be_disabled()

    @allure.step("Check the button is enabled")
    def should_have_enabled_button(self):
        expect(self.button).to_be_enabled()

    @allure.step("Select the option: {option}")
    def choose_select_option(self, option):
        self.select.select_option(option)
