from playwright.sync_api import Page, expect
from pages.inputs.base_input_page import InputBasePage


class InputPasswdPage(InputBasePage):
    URL = "https://www.qa-practice.com/elements/input/passwd"

    def __init__(self, page: Page):
        super().__init__(page, "#id_password", "#error_1_id_password")

