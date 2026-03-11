from playwright.sync_api import Page, expect
from pages.inputs.base_input_page import InputBasePage


class InputEmailPage(InputBasePage):
    URL = "https://www.qa-practice.com/elements/input/email"

    def __init__(self, page:Page) -> None:
        super().__init__(page, "#id_email", "#error_1_id_email")
