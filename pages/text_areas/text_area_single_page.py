from playwright.sync_api import Page, expect
from pages.text_areas.base_text_area_page import BaseTextAreaPage
import allure


class TextAreaSinglePage(BaseTextAreaPage):
    URL = "https://www.qa-practice.com/elements/textarea/single"

    def __init__(self, page: Page) -> None:
        super().__init__(page, "#error_1_id_text_area")
        self.text_area = page.locator("#id_text_area")


    @allure.step("Check text area page label and necessity")
    def should_have_default_state(self) -> None:
        expect(self.page.locator(f'label[for="id_text_area"]')).to_have_text("Text area*")
        self.should_have_required_area(self.text_area)


    @allure.step("Fill text: {text}")
    def fill(self, text: str) -> None:
        self.text_area.fill(text)






