import allure
from utils.allure_helper import attach_screenshot


@allure.feature("Simple button")
@allure.title("Checking button submit")
@allure.description("""
Requirements:
- The user should be able to click the button.
- The button should be labeled Click.
- After pressing the button, the user should be shown confirmation that the button was pressed.
""")
def test_simple_button_click_shows_confirmation(simple_button_page) -> None:
    try:
        simple_button_page.open()
        simple_button_page.should_have_button_labeled("Click")
        simple_button_page.click()
        simple_button_page.should_have_result_text("Submitted")
    except Exception as e:
        attach_screenshot(simple_button_page.page, "error_screenshot")
        raise e



