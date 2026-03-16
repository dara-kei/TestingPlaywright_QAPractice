from playwright.sync_api import Page, expect
from pages.checkboxes.base_checkbox_page import BaseCheckboxPage


class CheckboxesMultiplePage(BaseCheckboxPage):
    URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"

    def __init__(self, page: Page) ->None:
        super().__init__(page)
        self.checkboxes = [
            page.locator("#id_checkboxes_0"),
            page.locator("#id_checkboxes_1"),
            page.locator("#id_checkboxes_2"),
        ]


    def should_have_default_state(self):
        expect(self.page.locator('input[type = "checkbox"]')).to_have_count(3)  # проверяем, что на странице 3 чекбокса
        expect(self.page.locator('label[for = "id_checkboxes_0"]')).to_have_text("One")  # проверяем названия чекбоксов
        expect(self.page.locator('label[for = "id_checkboxes_1"]')).to_have_text("Two")
        expect(self.page.locator('label[for = "id_checkboxes_2"]')).to_have_text("Three")
        self.should_have_button_named("Submit")
        self.should_have_button_enabled()


    def select_checkbox(self, checkbox_index):
        self.checkboxes[checkbox_index].check()


    def should_have_checkbox_checked(self, checkbox_index):
        expect(self.checkboxes[checkbox_index]).to_be_checked()


