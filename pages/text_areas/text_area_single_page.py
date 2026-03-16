from playwright.sync_api import Page, expect
from pages.text_areas.base_text_area_page import BaseTextAreaPage


class TextAreaSinglePage(BaseTextAreaPage):
    URL = "https://www.qa-practice.com/elements/textarea/single"

    def __init__(self, page: Page) -> None:
        super().__init__(page, "#error_1_id_text_area")
        self.text_area = page.locator("#id_text_area")

    def should_have_default_state(self) -> None:
        expect(self.page.locator(f'label[for="id_text_area"]')).to_have_text("Text area*")
        expect(self.text_area).to_have_attribute("required", "")


    def fill(self, text: str) -> None:
        self.text_area.fill(text)






