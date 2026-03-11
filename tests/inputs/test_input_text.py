import pytest


# positive tests

def test_email_input_is_required_field(input_text_page)-> None:
    input_text_page.open()
    input_text_page.check_text_field_is_required()

@pytest.mark.parametrize("valid_text", ["hh", "Fgh77_-", "1234567890123456789012345"],
                         ids = ["min_length_text", "text_with_valid_symbols", "max_length_text"])
def test_valid_text_input_submission(input_text_page, valid_text)-> None:
    input_text_page.open()
    input_text_page.enter_text_input_and_submit(valid_text)
    input_text_page.result_text_should_be_visible()
    input_text_page.should_have_result_text(valid_text)


# negative tests

def test_empty_text_input_shows_validation_error(input_text_page)-> None:
    input_text_page.open()
    input_text_page.enter_text_input_and_submit("")
    assert input_text_page.validation_message() == "Please fill out this field."

def test_whitespace_only_input_shows_validation_error(input_text_page)-> None:
    input_text_page.open()
    input_text_page.enter_text_input_and_submit("  ")
    input_text_page.should_have_error_message("This field is required.")


def test_input_shorter_than_min_length_shows_validation_error(input_text_page)-> None:
    input_text_page.open()
    input_text_page.enter_text_input_and_submit("j")
    input_text_page.should_have_error_message("Please enter 2 or more characters")


def test_input_longer_than_max_length_shows_validation_error(input_text_page)-> None:
    input_text_page.open()
    input_text_page.enter_text_input_and_submit("12345678901234567890123456")
    input_text_page.should_have_error_message("Please enter no more than 25 characters")


@pytest.mark.parametrize("invalid_text", ["Привет", "@@"])
def test_invalid_characters_input_shows_validation_error(input_text_page, invalid_text)-> None:
    input_text_page.open()
    input_text_page.enter_text_input_and_submit(invalid_text)
    input_text_page.should_have_error_message("Enter a valid string consisting of letters, numbers, underscores or hyphens.")
