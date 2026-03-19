import allure
from utils.allure_helper import attach_screenshot


@allure.feature("Single text area")
@allure.title("Checking single text area default state")
@allure.description("""
Requirements:
- Field name is "Text area"
- This is a required field.
""")
def test_area_single_initial_state(text_area_single_page) -> None:
    try:
        text_area_single_page.open()
        text_area_single_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(text_area_single_page.page, "error_screenshot")
        raise e


@allure.feature("Single text area")
@allure.title("Checking submitting single text area")
@allure.description("""
Requirements:
- User should be able to enter any text into this field.
- The result can be sent using the Submit button.
- After submitting the form, the text entered by the user is displayed on the page.
""")
def test_submit_when_text_area_filled(text_area_single_page) -> None:
    try:
        text_area_single_page.open()
        text_area_single_page.fill("Hello!")
        text_area_single_page.submit()
        text_area_single_page.should_have_result_text("Hello!")
    except Exception as e:
        attach_screenshot(text_area_single_page.page, "error_screenshot")
        raise e


@allure.feature("Single text area")
@allure.title("Trying submitting single text area without filling any text")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_submit_when_text_area_not_filled(text_area_single_page) -> None:
    try:
        text_area_single_page.open()
        text_area_single_page.submit()
        text_area_single_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(text_area_single_page.page, "error_screenshot")
        raise e


@allure.feature("Single text area")
@allure.title("Trying submitting single text area with filling only spaces")
@allure.description("""
Requirements:
- This is a required field.
""")
def test_submit_when_text_area_filled_with_only_spaces(text_area_single_page) -> None:
    try:
        text_area_single_page.open()
        text_area_single_page.fill("  ")
        text_area_single_page.submit()
        text_area_single_page.should_have_error_message("This field is required.")
    except Exception as e:
        attach_screenshot(text_area_single_page.page, "error_screenshot")
        raise e




