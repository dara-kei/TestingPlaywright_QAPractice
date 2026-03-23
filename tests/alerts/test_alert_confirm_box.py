import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Alert confirmation box")
@allure.title("Checking button display")
@allure.description("""
Requirements:
- The page should have a Click button
""")
def test_page_have_click_button(alert_confirmation_box_page) -> None:
    try:
        alert_confirmation_box_page.open()
        alert_confirmation_box_page.should_have_button_visible()
    except Exception as err:
        attach_screenshot(alert_confirmation_box_page.page, "error_screenshot")
        raise err


@pytest.mark.positive
@allure.feature("Alert confirmation box")
@allure.title("Checking alert dialog data and accepting it.")
@allure.description("""
Requirements:
- When the button is clicked, an alert is displayed to the user.
- Alert window should display text "I am an alert!"
- The alert should have an OK button.
- After clicking on the OK button, the alert should be closed.
- The user's choice should be displayed on the page.
""")
def test_confirm_dialog_info_and_accept(alert_confirmation_box_page) -> None:
    try:
        alert_confirmation_box_page.open()
        alert_confirmation_box_page.check_alert_dialog_and_accept("confirm", "Select Ok or Cancel")
        alert_confirmation_box_page.should_have_result_text("Ok")
    except Exception as err:
        attach_screenshot(alert_confirmation_box_page.page, "error_screenshot")
        raise err


@pytest.mark.positive
@allure.feature("Alert confirmation box")
@allure.title("Checking cancellation alert dialog.")
@allure.description("""
Requirements:
- The alert should have a Cancel button.
- After clicking on the Cancel button, the alert should be closed.
- The user's choice should be displayed on the page.
""")
def test_confirm_dialog_cancel(alert_confirmation_box_page) -> None:
    try:
        alert_confirmation_box_page.open()
        alert_confirmation_box_page.alert_dialog_dismiss()
        alert_confirmation_box_page.should_have_result_text("Cancel")
    except Exception as err:
        attach_screenshot(alert_confirmation_box_page.page, "error_screenshot")
        raise err


