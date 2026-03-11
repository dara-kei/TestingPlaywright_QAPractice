from playwright.sync_api import Page, expect
from pages.buttons.base_button_page import BaseButtonPage


class LooksLikeAButtonPage(BaseButtonPage):
    URL = "https://www.qa-practice.com/elements/button/like_a_button"

    def __init__(self, page: Page) -> None:
        super().__init__(page, ".a-button")

