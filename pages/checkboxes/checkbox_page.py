from playwright.sync_api import Page, expect
from pages.checkboxes.base_checkbox_page import BaseCheckboxPage


class CheckboxPage(BaseCheckboxPage):
    URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkbox = page.locator("#id_checkbox_0")

    def select_checkbox(self):
        self.checkbox.check()

    def should_have_one_checkbox(self):
        expect(self.page.get_by_role("checkbox")).to_have_count(1)

    def should_have_checkbox_with_text(self, text):
        expect(self.page.locator('label[for="id_checkbox_0"]')).to_have_text(text)

    def should_have_checkbox_checked(self):
        expect(self.checkbox).to_be_checked()

    def should_have_default_state(self):
        self.should_have_one_checkbox()
        self.should_have_checkbox_with_text("Select me or not")
        self.should_have_button_named("Submit")
        self.should_have_button_enabled()




