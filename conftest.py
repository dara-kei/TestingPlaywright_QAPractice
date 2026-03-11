from playwright.sync_api import Page
from pages.inputs.input_text_page import InputTextPage
from pages.inputs.input_email_page import InputEmailPage
from pages.inputs.input_password_page import InputPasswdPage
from pages.buttons.simple_button_page import SimpleButtonPage
from pages.buttons.looks_like_a_button_page import LooksLikeAButtonPage
from pages.buttons.disabled_button_page import DisabledButtonPage


from pages.drop_down_page import DropDownPage

from pages.text_areas_multiple_page import TextAreasPage
from pages.checkbox_page import CheckboxPage
import pytest


@pytest.fixture
def input_text_page(page: Page):
    return InputTextPage(page)

@pytest.fixture
def input_email_page(page: Page):
    return InputEmailPage(page)

@pytest.fixture
def input_passwd_page(page: Page):
    return InputPasswdPage(page)

@pytest.fixture
def simple_button_page(page: Page):
    return SimpleButtonPage(page)

@pytest.fixture
def looks_like_button_page(page: Page):
    return LooksLikeAButtonPage(page)

@pytest.fixture
def disabled_button_page(page: Page):
    return DisabledButtonPage(page)

@pytest.fixture
def select_page(page: Page):
    return DropDownPage(page)

@pytest.fixture
def text_areas_page(page: Page):
    return TextAreasPage(page)

@pytest.fixture
def checkbox_page(page: Page):
    return CheckboxPage(page)