from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class BaseTextAreaPage(BasePage):
    def __init__(self, page, error_locator: str):
        super().__init__(page)
        self.button = page.locator("#submit-id-submit")
        self.result = page.locator("#result-text")
        self.error = page.locator(error_locator)

    def submit(self):
        self.button.click()

    def should_have_result_text(self, expected):
        expect(self.result).to_have_text(expected)

    def should_not_have_result(self):
        expect(self.result).to_have_count(0)


    def areas_should_have_correct_labels(self):
        expect(self.page.locator('label[for="id_first_chapter"]')).to_have_text("First chapter*")
        expect(self.page.locator('label[for="id_second_chapter"]')).to_have_text("Second chapter")
        expect(self.page.locator('label[for="id_third_chapter"]')).to_have_text("Third chapter")


    def page_should_have_three_text_areas(self):
        expect(self.page.locator("textarea")).to_have_count(3)


    def should_have_required_area(self, text_area):
        expect(text_area).to_have_attribute("required", "")


    def should_have_error_message(self, error_message):
        expect(self.error).to_have_text(error_message)

