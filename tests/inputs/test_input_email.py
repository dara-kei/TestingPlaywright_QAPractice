import pytest
import allure
from utils.allure_helper import attach_screenshot


# positive tests

@allure.feature("Input email")
@allure.title("Checking input email field submission")
@allure.description("""
Requirements:
- This is a required field.
- Entered text should be a valid email address.
- "localhost" domain should be allowed.
- User can submit this one-field form by pressing Enter.
- After submitting the form, the text entered by the user is displayed on the page.
""")
@pytest.mark.parametrize('valid_email', ["user@google.com", "user@localhost", " user@localhost "])
def test_valid_email_input_submission(input_email_page, valid_email)-> None:
    try:
        input_email_page.open()
        input_email_page.check_text_field_is_required()
        input_email_page.enter_text_input_and_submit(valid_email)
        input_email_page.result_text_should_be_visible()
        input_email_page.should_have_result_text(valid_email)
    except Exception as e:
        attach_screenshot(input_email_page.page, "error_screenshot")
        raise e


# negative tests

@allure.feature("Input email")
@allure.title("Trying submitting input email field without filling data")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_empty_email_input_shows_error_message(input_email_page)-> None:
    try:
        input_email_page.open()
        input_email_page.enter_text_input_and_submit("")
        input_email_page.should_have_validation_message("Please fill out this field.")
    except Exception as e:
        attach_screenshot(input_email_page.page, "error_screenshot")
        raise e


@allure.feature("Input email")
@allure.title("Trying submitting input email field with whitespace only")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_whitespace_only_email_input_shows_error_message(input_email_page)-> None:
    try:
        input_email_page.open()
        input_email_page.enter_text_input_and_submit("  ")
        input_email_page.should_have_error_message("This field is required.")
    except Exception as e:
        attach_screenshot(input_email_page.page, "error_screenshot")
        raise e


@allure.feature("Input email")
@allure.title("Trying submitting input email field with invalid data")
@allure.description("""
Requirements:
- Entered text should be a valid email address.
- "localhost" domain should be allowed.
""")
@pytest.mark.parametrize("invalid_email", ["userlocalhost", "юсер@localhost"])
def test_invalid_characters_email_input_shows_validation_error(input_email_page,invalid_email)-> None:
    try:
        input_email_page.open()
        input_email_page.enter_text_input_and_submit(invalid_email)
        input_email_page.should_have_error_message("Enter a valid email address.")
    except Exception as e:
        attach_screenshot(input_email_page.page, "error_screenshot")
        raise e

