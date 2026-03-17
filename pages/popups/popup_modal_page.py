from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ModalPopupPage(BasePage):
    URL = "https://www.qa-practice.com/elements/popup/modal"
    def __init__(self, page: Page):
        super().__init__(page)
        self.button = page.locator("#content > button")
        self.popup = page.locator(".modal-content")
        self.result = page.locator("#result-text")


    def should_have_page_button_named(self, button_name):
        expect(self.button).to_have_text(button_name)

    def open_popup(self):
        self.button.click()

    def should_have_popup(self):
        expect(self.popup).to_be_visible()


    def should_have_popup_default_state(self):
        expect(self.popup.locator("#exampleModalLabel")).to_have_text("I am a Pop-Up")
        expect(self.popup.locator('label[for="id_checkbox_0"]')).to_have_text("Select me or not")
        expect(self.popup.locator(".modal-footer button")).to_have_count(2)
        expect(self.popup.locator(".modal-footer button[type='submit']")).to_have_text("Send")
        expect(self.popup.locator(".modal-footer button[type='button']")).to_have_text("Close")
        # не соответствие требованиям: There should be two buttons: "Cancel" and "Send"

    def submit_popup_with_checkbox_checked(self):
        self.popup.locator("#id_checkbox_0").check()
        self.popup.locator('button[type="submit"]').click()

    def should_have_result_text(self, text):
        expect(self.result).to_have_text(text)

    def should_not_have_result(self):
        expect(self.result).to_have_count(0)

    def submit_popup_with_checkbox_unchecked(self):
        expect(self.popup.locator("#id_checkbox_0")).not_to_be_checked()
        self.popup.locator('button[type="submit"]').click()


    def cancel_popup(self):
        self.popup.locator(".modal-footer button[type='button']").click()



