from pages.new_tabs.base_tabs_page import BaseTabPage
from playwright.sync_api import Page, expect


class NewTabWithButtonPage(BaseTabPage):
    URL = "https://www.qa-practice.com/elements/new_tab/button"
    NEW_URL = "https://www.qa-practice.com/elements/new_tab/new_page"
    def __init__(self, page: Page):
        super().__init__(page, "#new-page-button")


    def check_new_page(self):
        new_page = self.open_new_page()
        expect(new_page).to_have_url(self.NEW_URL)
        expect(new_page.locator("#result-text")).to_have_text("I am a new page in a new tab")