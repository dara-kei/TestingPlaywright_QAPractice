import pytest
import allure
from utils.allure_helper import attach_screenshot


@pytest.mark.positive
@allure.feature("Input password")
@allure.title("Checking input password field submission")
@allure.description("""
Requirements:
- This is a required field.
- Has minimum 8 characters in length.
- At least one uppercase English letter.
- At least one lowercase English letter.
- At least one digit.
- At least one special character.
- User can submit this one-field form by pressing Enter.
- After submitting the form, the text entered by the user is displayed on the page.
""")
@pytest.mark.parametrize("valid_passwd", ["Tested1#", "Tested1#привет", "&&&&!%$@Tested66789"])
def test_valid_passwd_input_submission(input_passwd_page,valid_passwd)-> None:
    try:
        input_passwd_page.open()
        input_passwd_page.check_text_field_is_required()
        input_passwd_page.enter_text_input_and_submit(valid_passwd)
        input_passwd_page.result_text_should_be_visible()
        input_passwd_page.should_have_result_text(valid_passwd)
    except Exception as e:
        attach_screenshot(input_passwd_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
@allure.feature("Input password")
@allure.title("Trying submitting empty input password")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_empty_text_input_shows_validation_error(input_passwd_page)-> None:
    try:
        input_passwd_page.open()
        input_passwd_page.enter_text_input_and_submit("")
        input_passwd_page.should_have_validation_message("Please fill out this field.")
    except Exception as e:
        attach_screenshot(input_passwd_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
@allure.feature("Input password")
@allure.title("Trying submitting input password field with whitespace only")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_whitespace_only_input_shows_validation_error(input_passwd_page)-> None:
    try:
        input_passwd_page.open()
        input_passwd_page.enter_text_input_and_submit("  ")
        input_passwd_page.should_have_error_message("This field is required.")
    except Exception as e:
        attach_screenshot(input_passwd_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
@allure.feature("Input password")
@allure.title("Trying submitting input password field with invalid data")
@allure.description("""
Requirements:
- Has minimum 8 characters in length.
- At least one uppercase English letter.
- At least one lowercase English letter.
- At least one digit.
- At least one special character.
""")
@pytest.mark.parametrize("invalid_passwd", ["tested1#", "Tested11", "Tested##", "Test1#"],
                         ids = ["passwd_without_one_uppercase_let",
                                "passwd_without_special_symbol",
                                "passwd_without_numbers",
                                "passwd_shorter_than_min_length"])
def test_invalid_passwd_input_shows_error_message(input_passwd_page, invalid_passwd)-> None:
    try:
        input_passwd_page.open()
        input_passwd_page.enter_text_input_and_submit(invalid_passwd)
        input_passwd_page.should_have_error_message("Low password complexity")
    except Exception as e:
        attach_screenshot(input_passwd_page.page, "error_screenshot")
        raise e


