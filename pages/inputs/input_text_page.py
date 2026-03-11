from playwright.sync_api import Page, expect
from pages.inputs.base_input_page import InputBasePage


class InputTextPage(InputBasePage):
    URL = "https://www.qa-practice.com/elements/input/simple"

    def __init__(self, page: Page):
        super().__init__(page, "#id_text_string", "#error_1_id_text_string")




