from pages.new_tabs.base_tabs_page import BaseTabPage
from playwright.sync_api import Page, expect


class NewTabLinkPage(BaseTabPage):
    URL = "https://www.qa-practice.com/elements/new_tab/link"
    NEW_URL = "https://www.qa-practice.com/elements/new_tab/new_page"

    def __init__(self, page: Page):
        super().__init__(page, "#new-page-link")





