import pytest


# positive tests

def test_text_input_is_required_field(input_email_page)-> None:
    input_email_page.open()
    input_email_page.check_text_field_is_required()


@pytest.mark.parametrize('valid_email', ["user@google.com", "user@localhost", " user@localhost "])
def test_valid_email_input_submission(input_email_page, valid_email)-> None:
    input_email_page.open()
    input_email_page.enter_text_input_and_submit(valid_email)
    input_email_page.result_text_should_be_visible()
    input_email_page.should_have_result_text(valid_email)


# negative tests


def test_empty_email_input_shows_error_message(input_email_page)-> None:
    input_email_page.open()
    input_email_page.enter_text_input_and_submit("")
    assert input_email_page.validation_message() == "Please fill out this field."


def test_whitespace_only_email_input_shows_error_message(input_email_page)-> None:
    input_email_page.open()
    input_email_page.enter_text_input_and_submit("  ")
    input_email_page.should_have_error_message("This field is required.")


@pytest.mark.parametrize("invalid_email", ["userlocalhost", "юсер@localhost"])
def test_invalid_characters_email_input_shows_validation_error(input_email_page,invalid_email)-> None:
    input_email_page.open()
    input_email_page.enter_text_input_and_submit(invalid_email)
    input_email_page.should_have_error_message("Enter a valid email address.")

