import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Alert prompt box")
@allure.title("Checking button display")
@allure.description("""
Requirements:
- The page should have a Click button
""")
def test_page_have_click_button(alert_prompt_box_page) -> None:
    try:
        alert_prompt_box_page.open()
        alert_prompt_box_page.should_have_button_visible()
    except Exception as err:
        attach_screenshot(alert_prompt_box_page.page, "error_screenshot")
        raise err


@pytest.mark.positive
@allure.feature("Alert prompt box")
@allure.title("Checking prompt dialog data and accepting it.")
@allure.description("""
Requirements:
- When the button is clicked, an alert is displayed to the user.
- Alert window should display text "I am an alert!".
- The alert should have an OK button and a text input field.
- After clicking on the OK button, the alert should be closed.
- The user's input should be displayed on the page.
""")
def test_prompt_dialog_info_and_accept(alert_prompt_box_page) -> None:
    try:
        alert_prompt_box_page.open()
        alert_prompt_box_page.check_alert_dialog_and_accept("prompt", "Please enter some text", prompt_text="Hello!")
        alert_prompt_box_page.should_have_result_text("Hello!")
    except Exception as err:
        attach_screenshot(alert_prompt_box_page.page, "error_screenshot")
        raise err



@pytest.mark.positive
@allure.feature("Alert prompt box")
@allure.title("Checking cancellation alert dialog.")
@allure.description("""
Requirements:
- The alert should have a Cancel button.
- After clicking on the Cancel button, the alert should be closed.
- The user's input should be displayed on the page.
""")
def test_prompt_dialog_cancel(alert_prompt_box_page) -> None:
    try:
        alert_prompt_box_page.open()
        alert_prompt_box_page.alert_dialog_dismiss()
        alert_prompt_box_page.should_have_result_text("You canceled the prompt")
    except Exception as err:
        attach_screenshot(alert_prompt_box_page.page, "error_screenshot")
        raise err



