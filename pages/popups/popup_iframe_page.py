from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class IframePopupPage(BasePage):
    URL = "https://www.qa-practice.com/elements/popup/iframe_popup"
    def __init__(self, page: Page):
        super().__init__(page)
        self.button_open_popup = page.locator("#content > button")
        self.input_form = page.locator("#id_text_from_iframe")
        self.button_submit_input_form = page.locator("#submit-id-submit")
        self.result = page.locator("#check-result")
        self.popup_title = page.frame_locator("iframe.embed-responsive-item").locator("h1")
        self.popup_text_to_copy = page.frame_locator("iframe.embed-responsive-item").locator("#text-to-copy")
        self.popup_buttons = page.locator(".modal-footer button")
        self.popup_close_button = page.locator(".modal-footer button[type='button']")
        self.popup_check_button = page.locator(".modal-footer button[type='submit']")


    def should_have_button_open_popup_named(self, button_name):
        expect(self.button_open_popup).to_have_text(button_name)

    def open_popup(self):
        self.button_open_popup.click()

    def get_iframe_text(self):
        return self.popup_text_to_copy.inner_text()


    def should_have_popup_default_state(self):
        expect(self.popup_title).to_be_visible(timeout=10000)
        expect(self.popup_title).to_have_text("Iframe page title")
        expect(self.popup_text_to_copy).to_have_text("I am the text you want to copy")
        expect(self.popup_buttons).to_have_count(2)
        expect(self.popup_check_button).to_have_text("Check")
        expect(self.popup_close_button).to_have_text("Close")
        # не соответствие требованиям: There should be two buttons: "Cancel" and "Send"

    def click_check(self):
        self.popup_check_button.click()

    def click_close(self):
        self.popup_close_button.click()


    def should_have_input_form_default_state(self):
        expect(self.input_form).to_be_visible()
        expect(self.button_submit_input_form).to_be_visible()

    def fill_input_form(self, text):
        self.input_form.fill(text)

    def submit_input_form(self):
        self.button_submit_input_form.click()

    def should_have_result_text(self, text):
        expect(self.result).to_have_text(text)

    def should_not_have_result(self):
        expect(self.result).to_have_count(0)
