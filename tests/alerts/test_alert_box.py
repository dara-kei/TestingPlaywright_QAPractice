import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Alert")
@allure.title("Checking button display")
@allure.description("""
Requirements:
- The page should have a Click button.
""")
def test_page_have_click_button(alert_box_page) -> None:
    try:
        alert_box_page.open()
        alert_box_page.should_have_button_visible()
    except Exception as err:
        attach_screenshot(alert_box_page.page, "error_screenshot")
        raise err



@pytest.mark.positive
@allure.feature("Alert")
@allure.title("Checking alert dialog data and accepting it.")
@allure.description("""
Requirements:
- When the button is clicked, an alert is displayed to the user.
- Alert window should display text "I am an alert!"
- The alert should have an OK button.
- After clicking on the OK button, the alert should be closed.
""")
def test_alert_box_appear(alert_box_page) -> None:
    try:
        alert_box_page.open()
        alert_box_page.check_alert_dialog_and_accept("alert", "I am an alert!")
    except Exception as err:
        attach_screenshot(alert_box_page.page, "error_screenshot")
        raise err

