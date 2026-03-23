import pytest
import allure
from utils.allure_helper import attach_screenshot


@pytest.mark.positive
@allure.feature("Iframe Pop-Up")
@allure.title("Checking button that opens Pop-Up")
@allure.description("""
Requirements:
- There should be a button named "Launch Pop-Up".
""")
def test_name_of_button_that_open_popup(popup_iframe_page):
    try:
        popup_iframe_page.open()
        popup_iframe_page.should_have_button_open_popup_named("Launch Pop-Up")
    except Exception as e:
        attach_screenshot(popup_iframe_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@pytest.mark.xfail(reason="Bug: wrong name for a button", strict=False)
@allure.feature("Iframe Pop-Up")
@allure.title("Checking Pop-Up default state")
@allure.description("""
Requirements:
- The Pop-Up:
- There should be an iframe page in the Pop-Up.
- The page title should be "Iframe page title".
- There should be a text to copy "I am the text you want to copy".
- There should be two buttons: "Cancel" and "Check".
""")
def test_popup_initial_state(popup_iframe_page):
    try:
        popup_iframe_page.open()
        popup_iframe_page.open_popup()
        popup_iframe_page.should_have_popup_default_state()
    except Exception as e:
        attach_screenshot(popup_iframe_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Iframe Pop-Up")
@allure.title("Checking input form default state")
@allure.description("""
Requirements:
- The form should consist of one input field and a submit button.
""")
def test_input_form_initial_state(popup_iframe_page):
    try:
        popup_iframe_page.open()
        popup_iframe_page.open_popup()
        popup_iframe_page.click_check()
        popup_iframe_page.should_have_input_form_default_state()
    except Exception as e:
        attach_screenshot(popup_iframe_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Iframe Pop-Up")
@allure.title("Checking submitting input form with valid data")
@allure.description("""
Requirements:
- After submitting the form, the user input should be validated and the result should be displayed on the page.
- If the user entered the correct text, a green element with the text "Correct!" should be displayed.
""")
def test_submit_input_form_with_valid_data(popup_iframe_page):
    try:
        popup_iframe_page.open()
        popup_iframe_page.open_popup()
        text = popup_iframe_page.get_iframe_text()
        popup_iframe_page.click_check()
        popup_iframe_page.fill_input_form(text)
        popup_iframe_page.submit_input_form()
        popup_iframe_page.should_have_result_text("Correct!")
    except Exception as e:
        attach_screenshot(popup_iframe_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
@allure.feature("Iframe Pop-Up")
@allure.title("Checking submitting input form with invalid data")
@allure.description("""
Requirements:
- If the user entered incorrect text, a yellow element with the text "Nope. Better luck next time!" should be displayed.
""")
@pytest.mark.parametrize("invalid_data", ["  ", "hglhhkjnk", "*"])
def test_submit_input_form_with_invalid_data(popup_iframe_page, invalid_data):
    try:
        popup_iframe_page.open()
        popup_iframe_page.open_popup()
        popup_iframe_page.click_check()
        popup_iframe_page.fill_input_form(invalid_data)
        popup_iframe_page.submit_input_form()
        popup_iframe_page.should_have_result_text("Nope. Better luck next time!")
    except Exception as e:
        attach_screenshot(popup_iframe_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Iframe Pop-Up")
@allure.title("Checking canceling Pop-Up")
@allure.description("""
Requirements:
- Clicking Cancel close Pop-up.
""")
def test_cancel_iframe_popup(popup_iframe_page):
    try:
        popup_iframe_page.open()
        popup_iframe_page.open_popup()
        popup_iframe_page.click_close()
        popup_iframe_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(popup_iframe_page.page, "error_screenshot")
        raise e
