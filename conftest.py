from playwright.sync_api import Page
from pages.drop_down_page import DropDownPage
from pages.text_areas_multiple_page import TextAreasPage
from pages.checkbox_page import CheckboxPage
import pytest


@pytest.fixture
def select_page(page: Page):
    return DropDownPage(page)

@pytest.fixture
def text_areas_page(page: Page):
    return TextAreasPage(page)

@pytest.fixture
def checkbox_page(page: Page):
    return CheckboxPage(page)