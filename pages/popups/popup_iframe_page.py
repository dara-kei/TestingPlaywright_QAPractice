from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


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


    @allure.step("Check button name")
    def should_have_button_open_popup_named(self, button_name):
        expect(self.button_open_popup).to_have_text(button_name)


    @allure.step("Open Pop-Up iframe")
    def open_popup(self):
        self.button_open_popup.click()


    @allure.step("Get Pop-Up iframe text")
    def get_iframe_text(self):
        return self.popup_text_to_copy.inner_text()


    @allure.step("Check Pop-Up modal default state")
    def should_have_popup_default_state(self):
        with allure.step("Check an iframe page in the Pop-Up"):
            expect(self.popup_title).to_be_visible()
        with allure.step("Check page title is 'Iframe page title'"):
            expect(self.popup_title).to_have_text("Iframe page title")
        with allure.step("Check a text to copy is 'I am the text you want to copy'"):
            expect(self.popup_text_to_copy).to_have_text("I am the text you want to copy")
        with allure.step("Check buttons on the Pop-Up"):
            expect(self.popup_buttons).to_have_count(2)
            expect(self.popup_check_button).to_have_text("Check")
            expect(self.popup_close_button).to_have_text("Cancel")


    @allure.step("Click check button on Pop-Up iframe")
    def click_check(self):
        self.popup_check_button.click()


    @allure.step("Click cancel button on Pop-Up iframe")
    def click_close(self):
        self.popup_close_button.click()


    @allure.step("Check form should consist of one input field and a submit button")
    def should_have_input_form_default_state(self):
        expect(self.input_form).to_be_visible()
        expect(self.button_submit_input_form).to_be_visible()


    @allure.step("Fill input form")
    def fill_input_form(self, text):
        self.input_form.fill(text)


    @allure.step("Submit input form")
    def submit_input_form(self):
        self.button_submit_input_form.click()


    @allure.step("Check result text is {text}")
    def should_have_result_text(self, text):
        expect(self.result).to_have_text(text)


    @allure.step("Check result is not displayed")
    def should_not_have_result(self):
        expect(self.result).to_have_count(0)
