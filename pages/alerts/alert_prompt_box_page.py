from pages.alerts.base_alert_page import BaseAlertPage
from playwright.sync_api import Page


class AlertPromptBoxPage(BaseAlertPage):
    URL = "https://www.qa-practice.com/elements/alert/prompt"
    def __init__(self, page: Page) -> None:
        super().__init__(page)
