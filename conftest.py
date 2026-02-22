from playwright.sync_api import Page, expect
from pages.drop_down_page import DropDownPage
import pytest


@pytest.fixture
def select_page(page: Page):
    return DropDownPage(page)
    dd_page.open_url()