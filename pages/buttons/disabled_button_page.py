from playwright.sync_api import Page, expect
from pages.buttons.base_button_page import BaseButtonPage


class DisabledButtonPage(BaseButtonPage):
    URL = "https://www.qa-practice.com/elements/button/disabled"

    def __init__(self, page: Page) -> None:
        super().__init__(page, "#submit-id-submit")
        self.select = page.locator("#id_select_state")

    def should_have_disabled_button(self):
        expect(self.button).to_be_disabled()

    def should_have_enabled_button(self):
        expect(self.button).to_be_enabled()

    def choose_select_option(self, option):
        self.select.select_option(option)
