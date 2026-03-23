import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Disabled button")
@allure.title("Checking button is disabled")
@allure.description("""
Requirements:
- Submit button should be disabled by default.
""")
def test_button_is_disabled_by_default(disabled_button_page) -> None:
    try:
        disabled_button_page.open()
        disabled_button_page.should_have_disabled_button()
    except Exception as e:
        attach_screenshot(disabled_button_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Disabled button")
@allure.title("Checking button can change enabled/disabled state")
@allure.description("""
Requirements:
- User should be able to enable and then disable the button using the options of the Select state dropdown.
- The option selected in the dropdown should be applied to the button immediately.
""")
def test_button_state_can_be_changed_via_dropdown(disabled_button_page) -> None:
    try:
        disabled_button_page.open()
        disabled_button_page.choose_select_option("Enabled")
        disabled_button_page.should_have_enabled_button()
        disabled_button_page.choose_select_option("Disabled")
        disabled_button_page.should_have_disabled_button()
    except Exception as e:
        attach_screenshot(disabled_button_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Disabled button")
@allure.title("Checking button submit")
@allure.description("""
Requirements:
- After pressing the button, the user should be shown confirmation that the button was pressed.
""")
def test_button_click_shows_confirmation(disabled_button_page) -> None:
    try:
        disabled_button_page.open()
        disabled_button_page.choose_select_option("Enabled")
        disabled_button_page.click()
        disabled_button_page.should_have_result_text("Submitted")
    except Exception as e:
        attach_screenshot(disabled_button_page.page, "error_screenshot")
        raise e
