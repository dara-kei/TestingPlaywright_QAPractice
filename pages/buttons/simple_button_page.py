from playwright.sync_api import Page, expect
from pages.buttons.base_button_page import BaseButtonPage

class SimpleButtonPage(BaseButtonPage):
    URL = "https://www.qa-practice.com/elements/button/simple"

    def __init__(self, page: Page) -> None:
        super().__init__(page, "#submit-id-submit")

