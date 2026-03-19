import pytest
import allure
from utils.allure_helper import attach_screenshot


# positive tests

@allure.feature("Input text")
@allure.title("Checking input text field submission")
@allure.description("""
Requirements:
- This is a required field
- User should be able to enter text into this field
- Text should be a valid string consisting of English letters, numbers, underscores or hyphens
- Text length limits:
- Max: 25 characters
- Min: 2 characters
- User can submit this one-field form by pressing Enter
- After submitting the form, the text entered by the user is displayed on the page
""")
@pytest.mark.parametrize("valid_text", ["hh", "Fgh77_-", "1234567890123456789012345"],
                         ids = ["min_length_text", "text_with_valid_symbols", "max_length_text"])
def test_valid_text_input_submission(input_text_page, valid_text)-> None:
    try:
        input_text_page.open()
        input_text_page.check_text_field_is_required()
        input_text_page.enter_text_input_and_submit(valid_text)
        input_text_page.result_text_should_be_visible()
        input_text_page.should_have_result_text(valid_text)
    except Exception as e:
        attach_screenshot(input_text_page.page, "error_screenshot")
        raise e


# negative tests
@allure.feature("Input text")
@allure.title("Trying submitting input text field without filling data")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_empty_text_input_shows_validation_error(input_text_page)-> None:
    try:
        input_text_page.open()
        input_text_page.enter_text_input_and_submit("")
        input_text_page.should_have_validation_message("Please fill out this field.")
    except Exception as e:
        attach_screenshot(input_text_page.page, "error_screenshot")
        raise e


@allure.feature("Input text")
@allure.title("Trying submitting input text field with whitespace only")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_whitespace_only_input_shows_validation_error(input_text_page)-> None:
    try:
        input_text_page.open()
        input_text_page.enter_text_input_and_submit("  ")
        input_text_page.should_have_error_message("This field is required.")
    except Exception as e:
        attach_screenshot(input_text_page.page, "error_screenshot")
        raise e


@allure.feature("Input text")
@allure.title("Trying submitting input text field with invalid data")
@allure.description("""
Requirements:
- Has minimum 8 characters in length.
- At least one uppercase English letter.
- At least one lowercase English letter.
- At least one digit.
- At least one special character.
""")
@pytest.mark.parametrize("invalid_data, error_message", [("j", "Please enter 2 or more characters"),
                                                         ("12345678901234567890123456", "Please enter no more than 25 characters"),
                                                         ("Привет", "Enter a valid string consisting of letters, numbers, underscores or hyphens."),
                                                         ("@@", "Enter a valid string consisting of letters, numbers, underscores or hyphens.")])
def test_invalid_data_input_shows_validation_error(input_text_page, invalid_data, error_message)-> None:
    try:
        input_text_page.open()
        input_text_page.enter_text_input_and_submit(invalid_data)
        input_text_page.should_have_error_message(error_message)
    except Exception as e:
        attach_screenshot(input_text_page.page, "error_screenshot")
        raise e

