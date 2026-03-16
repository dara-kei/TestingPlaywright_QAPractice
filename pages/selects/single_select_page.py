from playwright.sync_api import Page, expect
from pages.selects.base_select_page import BaseSelectPage


class SingleSelectPage(BaseSelectPage):
    URL = "https://www.qa-practice.com/elements/select/single_select"


    def __init__(self, page: Page):
        super().__init__(page)
        self.select = page.locator("#id_choose_language")
        self.field_name = page.locator("label[for='id_choose_language']")


    def choose_select_option(self, option: str) -> None:
        self.select.select_option(option)


    def should_have_default_state(self):
        expect(self.select).to_have_attribute("required", "")
        expect(self.page.locator("label[for='id_choose_language']")).to_have_text("Choose language*")
