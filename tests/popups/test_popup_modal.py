import allure
from utils.allure_helper import attach_screenshot
import pytest


@allure.feature("Modal Pop-Up")
@allure.title("Checking button that opens Pop-Up")
@allure.description("""
Requirements:
- There should be a button named "Launch Pop-Up".
""")
def test_name_of_button_that_open_popup(popup_modal_page):
    try:
        popup_modal_page.open()
        popup_modal_page.should_have_page_button_named("Launch Pop-Up")
    except Exception as e:
        attach_screenshot(popup_modal_page.page, "error_screenshot")
        raise e


@pytest.mark.xfail(reason="Bug: wrong name for a button", strict=False)
@allure.feature("Modal Pop-Up")
@allure.title("Checking Pop-Up default state")
@allure.description("""
Requirements:
- The Pop-Up:
- The Pop-Up title should be "I am a Pop-Up".
- There should be a checkbox "Select me or not" on the Pop-Up.
- There should be two buttons: "Cancel" and "Send".
""")
def test_popup_initial_state(popup_modal_page):
    try:
        popup_modal_page.open()
        popup_modal_page.open_popup()
        popup_modal_page.should_have_popup()
        popup_modal_page.should_have_popup_default_state()
    except Exception as e:
        attach_screenshot(popup_modal_page.page, "error_screenshot")
        raise e


@allure.feature("Modal Pop-Up")
@allure.title("Checking sending Pop-Up value with checkbox checked")
@allure.description("""
Requirements:
- Send button should send the value selected in the checkbox.
- The value sent from the Pop-Up should be displayed on the page in the "Selected checkboxes" section.
- The section "Selected checkboxes" should appear on the page only after sending a value from the Pop-Up.
""")
def test_send_popup_value_with_checkbox_checked(popup_modal_page):
    try:
        popup_modal_page.open()
        popup_modal_page.open_popup()
        popup_modal_page.submit_popup_with_checkbox_checked()
        popup_modal_page.should_have_result_text("select me or not")
    except Exception as e:
        attach_screenshot(popup_modal_page.page, "error_screenshot")
        raise e


@allure.feature("Modal Pop-Up")
@allure.title("Checking sending Pop-Up value without checkbox checked")
@allure.description("""
Requirements:
- Send button should send the value selected in the checkbox.
- The value sent from the Pop-Up should be displayed on the page in the "Selected checkboxes" section.
- The section "Selected checkboxes" should appear on the page only after sending a value from the Pop-Up.
""")
def test_send_popup_value_with_checkbox_unchecked(popup_modal_page):
    try:
        popup_modal_page.open()
        popup_modal_page.open_popup()
        popup_modal_page.submit_popup_with_checkbox_unchecked()
        popup_modal_page.should_have_result_text("None")
    except Exception as e:
        attach_screenshot(popup_modal_page.page, "error_screenshot")
        raise e


@allure.feature("Modal Pop-Up")
@allure.title("Checking canceling Pop-Up")
@allure.description("""
Requirements:
- The section "Selected checkboxes" should appear on the page only after sending a value from the Pop-Up.
""")
def test_cancel_popup(popup_modal_page):
    try:
        popup_modal_page.open()
        popup_modal_page.open_popup()
        popup_modal_page.cancel_popup()
        popup_modal_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(popup_modal_page.page, "error_screenshot")
        raise e

