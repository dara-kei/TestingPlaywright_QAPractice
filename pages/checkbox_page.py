from playwright.sync_api import Page, expect


class CheckboxPage:
    URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"

    def __init__(self, page: Page):
        self.page = page
        self.checkbox = page.locator("#id_checkbox_0")
        self.button = page.locator("#submit-id-submit")
        self.result = page.locator("#result-text")


    def open_page(self):
        self.page.goto(self.URL)

    def submit(self):
        self.button.click()

    def select_checkbox(self):
        self.checkbox.check()

    def checkbox_should_be_visible(self):
        expect(self.checkbox).to_be_visible()

    def checkbox_should_exist(self):
        expect(self.checkbox).to_have_count(1)

    def checkbox_should_have_text(self, text):
        expect(self.page.locator('label[for="id_checkbox_0"]')).to_have_text(text)

    def checkbox_should_be_checked(self):
        expect(self.checkbox).to_be_checked()

    def button_should_have_name(self, text):
        expect(self.button).to_have_value(text)

    def button_should_be_enable(self):
        expect(self.button).to_be_enabled()

    def result_should_have_text(self, text):
        expect(self.result).to_have_text(text)

    def result_should_not_exist(self):
        expect(self.result).to_have_count(0)