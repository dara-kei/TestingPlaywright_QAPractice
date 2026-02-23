from playwright.sync_api import Page, expect

URL = "https://www.qa-practice.com/elements/textarea/textareas"

class TextAreasPage:
    def __init__(self, page):
        self.page = page
        self.text_area_1 = page.locator("#id_first_chapter")
        self.text_area_2 = page.locator("#id_second_chapter")
        self.text_area_3 = page.locator("#id_third_chapter")
        self.button_loc = page.locator("#submit-id-submit")
        self.result_loc = page.locator("#result-text")


    def open_url(self):
        self.page.goto(URL)

    def submit(self):
        self.button_loc.click()

    def fill_areas(self, first = None, second = None, third = None):
        if first is not None:
            self.text_area_1.fill(first)
        if second is not None:
            self.text_area_2.fill(second)
        if third is not None:
            self.text_area_3.fill(third)

    def result_should_have_text(self, expected):
        expect(self.result_loc).to_have_text(expected)

    def result_should_not_exist(self):
        expect(self.result_loc).to_have_count(0)


    def areas_should_have_correct_labels(self):
        expect(self.page.locator('label[for="id_first_chapter"]')).to_have_text("First chapter*")
        expect(self.page.locator('label[for="id_second_chapter"]')).to_have_text("Second chapter")
        expect(self.page.locator('label[for="id_third_chapter"]')).to_have_text("Third chapter")


    def page_should_have_three_text_areas(self):
        expect(self.page.locator("textarea")).to_have_count(3)


    def first_area_should_be_required(self):
        expect(self.text_area_1).to_have_attribute("required", "")