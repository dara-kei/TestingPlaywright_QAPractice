from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class BaseDragAndDropPage(BasePage):
    def __init__(self, page : Page) -> None:
        super().__init__(page)

    def should_be_visible(self, locator):
        expect(locator).to_be_visible()

    def should_not_be_visible(self, locator):
        expect(locator).not_to_be_visible()

    def should_be_counted(self, locator, quantity):
        expect(locator).to_have_count(quantity)

    def should_have_result_text(self, locator, text):
        expect(locator).to_have_text(text)

    def drag_and_drop(self, drag_locator, drop_locator):
        drag_locator.drag_to(drop_locator)










