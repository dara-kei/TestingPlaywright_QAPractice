from playwright.sync_api import Page, expect, Dialog
from pages.base_page import BasePage


class BaseAlertPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.button = page.locator(".a-button")
        self.result = page.locator("#result-text")

    def click_button(self) -> None:
        self.button.click()

    def should_have_button_visible(self):
        expect(self.button).to_be_visible()

    def check_alert_dialog_and_accept(self, alert_type, alert_text, prompt_text=None) -> None:
        def handle_dialog(dialog: Dialog) -> None:
            assert dialog.type == alert_type
            assert alert_text in dialog.message
            if prompt_text is not None:
                dialog.accept(prompt_text)
            else:
                dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.click_button()

    def alert_dialog_dismiss(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())  # нажать cancel
        self.click_button()


    def should_have_result_text(self, text) -> None:
        expect(self.result).to_have_text(text)

