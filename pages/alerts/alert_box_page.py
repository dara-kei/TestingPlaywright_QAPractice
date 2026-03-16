from pages.alerts.base_alert_page import BaseAlertPage
from playwright.sync_api import Page


class AlertBoxPage(BaseAlertPage):
    URL = "https://www.qa-practice.com/elements/alert/alert"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

