from playwright.sync_api import Page, expect
from pages.text_areas.base_text_area_page import BaseTextAreaPage


class TextAreasMultiplePage(BaseTextAreaPage):
    URL = "https://www.qa-practice.com/elements/textarea/textareas"

    def __init__(self, page):
        super().__init__(page, "#error_1_id_first_chapter")
        self.text_areas = [page.locator("#id_first_chapter"),
                           page.locator("#id_second_chapter"),
                           page.locator("#id_third_chapter")]


    def fill_areas(self, first = None, second = None, third = None):
        if first is not None:
            self.text_areas[0].fill(first)
        if second is not None:
            self.text_areas[1].fill(second)
        if third is not None:
            self.text_areas[2].fill(third)


    def should_have_default_state(self):
        expect(self.page.locator("textarea")).to_have_count(3)
        expect(self.page.locator('label[for="id_first_chapter"]')).to_have_text("First chapter*")
        expect(self.page.locator('label[for="id_second_chapter"]')).to_have_text("Second chapter")
        expect(self.page.locator('label[for="id_third_chapter"]')).to_have_text("Third chapter")
        self.should_have_required_area(self.text_areas[0])


