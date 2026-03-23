import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Looks like a button")
@allure.title("Checking button submit")
@allure.description("""
Requirements:
- The user should be able to click the button.
- The button should be labeled Click.
- After pressing the button, the user should be shown confirmation that the button was pressed.
""")
def test_looks_like_a_button_click_shows_confirmation(looks_like_button_page) -> None:
    try:
        looks_like_button_page.open()
        looks_like_button_page.should_have_button_labeled("Click")
        looks_like_button_page.click()
        looks_like_button_page.should_have_result_text("Submitted")
    except Exception as e:
        attach_screenshot(looks_like_button_page.page, "error_screenshot")
        raise e