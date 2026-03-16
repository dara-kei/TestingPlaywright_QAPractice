from playwright.sync_api import Page
from pages.inputs.input_text_page import InputTextPage
from pages.inputs.input_email_page import InputEmailPage
from pages.inputs.input_password_page import InputPasswdPage
from pages.buttons.simple_button_page import SimpleButtonPage
from pages.buttons.looks_like_a_button_page import LooksLikeAButtonPage
from pages.buttons.disabled_button_page import DisabledButtonPage
from pages.checkboxes.checkbox_page import CheckboxPage
from pages.checkboxes.checkboxes_multiple_page import CheckboxesMultiplePage
from pages.selects.single_select_page import SingleSelectPage
from pages.selects.selects_multiple_page import SelectsMultiplePage
from pages.text_areas.text_areas_multiple_page import TextAreasMultiplePage
from pages.text_areas.text_area_single_page import TextAreaSinglePage
from pages.alerts.alert_box_page import AlertBoxPage
from pages.alerts.alert_confirmation_box_page import AlertConfirmationBoxPage
from pages.alerts.alert_prompt_box_page import AlertPromptBoxPage
from pages.new_tabs.new_tab_with_link_page import NewTabLinkPage
from pages.new_tabs.new_tab_with_button_page import NewTabWithButtonPage
from pages.drag_and_drop.drag_and_drop_boxes_page import DragAndDropBoxesPage
from pages.drag_and_drop.drag_and_drop_image_page import DragAndDropImagePage
from pages.iframe_page import IframePage

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
def checkbox_page(page: Page):
    return CheckboxPage(page)

@pytest.fixture
def checkboxes_multiple_page(page: Page):
    return CheckboxesMultiplePage(page)

@pytest.fixture
def single_select_page(page: Page):
    return SingleSelectPage(page)

@pytest.fixture
def select_multiple_page(page: Page):
    return SelectsMultiplePage(page)

@pytest.fixture
def text_areas_multiple_page(page: Page):
    return TextAreasMultiplePage(page)

@pytest.fixture
def text_area_single_page(page: Page):
        return TextAreaSinglePage(page)

@pytest.fixture
def alert_box_page(page: Page):
    return AlertBoxPage(page)

@pytest.fixture
def alert_confirmation_box_page(page: Page):
    return AlertConfirmationBoxPage(page)

@pytest.fixture
def alert_prompt_box_page(page: Page):
    return AlertPromptBoxPage(page)


@pytest.fixture
def new_tab_link_page(page: Page):
    return NewTabLinkPage(page)


@pytest.fixture
def new_tab_with_button_page(page: Page):
    return NewTabWithButtonPage(page)

@pytest.fixture
def drag_and_drop_boxes_page(page: Page):
    return DragAndDropBoxesPage(page)

@pytest.fixture
def drag_and_drop_image_page(page: Page):
    return DragAndDropImagePage(page)

@pytest.fixture
def iframe_page(page: Page):
    return IframePage(page)