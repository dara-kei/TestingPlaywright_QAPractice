from playwright.sync_api import Page, expect
from pages.checkboxes.base_checkbox_page import BaseCheckboxPage
import allure

class CheckboxesMultiplePage(BaseCheckboxPage):
    URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"

    def __init__(self, page: Page) ->None:
        super().__init__(page)
        self.checkboxes = [
            page.locator("#id_checkboxes_0"),
            page.locator("#id_checkboxes_1"),
            page.locator("#id_checkboxes_2"),
        ]


    @allure.step("Check the page default state")
    def should_have_default_state(self):
        with allure.step("Check checkboxes count"):
            expect(self.page.locator('input[type = "checkbox"]')).to_have_count(3)  # проверяем, что на странице 3 чекбокса
        with allure.step("Check checkboxes labels"):
            expect(self.page.locator('label[for = "id_checkboxes_0"]')).to_have_text("One")  # проверяем названия чекбоксов
            expect(self.page.locator('label[for = "id_checkboxes_1"]')).to_have_text("Two")
            expect(self.page.locator('label[for = "id_checkboxes_2"]')).to_have_text("Three")
        with allure.step("Check submit button"):
            self.should_have_button_named("Submit")
            self.should_have_button_enabled()


    @allure.step("Select the checkbox")
    def select_checkbox(self, checkbox_index):
        self.checkboxes[checkbox_index].check()


    @allure.step("Check the checkbox is checked")
    def should_have_checkbox_checked(self, checkbox_index):
        expect(self.checkboxes[checkbox_index]).to_be_checked()


