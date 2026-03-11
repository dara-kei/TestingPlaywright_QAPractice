import pytest


# positive tests

def test_passwd_input_is_required_field(input_passwd_page)-> None:
    input_passwd_page.open()
    input_passwd_page.check_text_field_is_required()

@pytest.mark.parametrize("valid_passwd", ["Tested1#", "Tested1#привет", "&&&&!%$@Tested66789"])
def test_valid_passwd_input_submission(input_passwd_page,valid_passwd)-> None:
    input_passwd_page.open()
    input_passwd_page.enter_text_input_and_submit(valid_passwd)
    input_passwd_page.result_text_should_be_visible()
    input_passwd_page.should_have_result_text(valid_passwd)


# negative tests

def test_empty_text_input_shows_validation_error(input_passwd_page)-> None:
    input_passwd_page.open()
    input_passwd_page.enter_text_input_and_submit("")
    assert input_passwd_page.validation_message() == "Please fill out this field."

def test_whitespace_only_input_shows_validation_error(input_passwd_page)-> None:
    input_passwd_page.open()
    input_passwd_page.enter_text_input_and_submit("  ")
    input_passwd_page.should_have_error_message("This field is required.")


@pytest.mark.parametrize("invalid_passwd", ["tested1#", "Tested11", "Tested##", "Test1#"],
                         ids = ["passwd_without_one_uppercase_let",
                                "passwd_without_special_symbol",
                                "passwd _without_numbers",
                                "passwd_shorter_than_min_length"])
def test_invalid_passwd_input_shows_error_message(input_passwd_page, invalid_passwd)-> None:
    input_passwd_page.open()
    input_passwd_page.enter_text_input_and_submit(invalid_passwd)
    input_passwd_page.should_have_error_message("Low password complexity")


