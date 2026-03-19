import pytest
import allure
from utils.allure_helper import attach_screenshot


@allure.feature("Multiple text area")
@allure.title("Checking text areas default state")
@allure.description("""
Requirements:
- There should be 3 fields:
- First chapter
- Second chapter
- Third chapter
- The field First chapter is required.
""")
def test_areas_multiple_initial_state(text_areas_multiple_page) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e


# positive tests

@allure.feature("Multiple text area")
@allure.title("Checking submitting when first text area is filled")
@allure.description("""
Requirements:
- The field First chapter is required.
- User should be able to enter any text in each field.
- The result can be sent using the Submit button.
- After submitting the form, the text entered by the user into all fields is displayed on the page.
""")
def test_submit_when_first_area_filled(text_areas_multiple_page) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.fill_areas(first = "Hello")
        text_areas_multiple_page.submit()
        text_areas_multiple_page.should_have_result_text("Hello")
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple text area")
@allure.title("Checking submitting when two text areas are filled (included required)")
@allure.description("""
Requirements:
- The field First chapter is required.
- User should be able to enter any text in each field.
- The result can be sent using the Submit button.
- After submitting the form, the text entered by the user into all fields is displayed on the page.
""")
@pytest.mark.parametrize("second, third", [("World", None), (None, "World")])
def test_submit_when_two_areas_filled(text_areas_multiple_page, second, third) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.fill_areas(first="Hello", second = second, third = third)
        text_areas_multiple_page.submit()
        text_areas_multiple_page.should_have_result_text("HelloWorld")
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple text area")
@allure.title("Checking submitting when all text areas are filled")
@allure.description("""
Requirements:
- The field First chapter is required.
- User should be able to enter any text in each field.
- The result can be sent using the Submit button.
- After submitting the form, the text entered by the user into all fields is displayed on the page.
""")
def test_submit_when_all_areas_filled(text_areas_multiple_page) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.fill_areas(first = "Hello", second = "my", third = "World!")
        text_areas_multiple_page.submit()
        text_areas_multiple_page.should_have_result_text("HelloMyWorld!")
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e


# negative tests

@allure.feature("Multiple text area")
@allure.title("Trying submitting when all text areas are empty")
@allure.description("""
Requirements:
- The field First chapter is required.
""")
def test_submit_when_all_areas_empty(text_areas_multiple_page) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.submit()
        text_areas_multiple_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple text area")
@allure.title("Trying submitting when required text area is empty")
@allure.description("""
Requirements:
- The field First chapter is required.
""")
def test_submit_when_required_area_not_filled(text_areas_multiple_page) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.fill_areas(second = "my", third = "World")
        text_areas_multiple_page.submit()
        text_areas_multiple_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple text area")
@allure.title("Trying submitting when required text area is filled with only spaces")
@allure.description("""
Requirements:
- The field First chapter is required.
""")
def test_submit_when_first_text_area_filled_with_only_spaces(text_areas_multiple_page) -> None:
    try:
        text_areas_multiple_page.open()
        text_areas_multiple_page.fill_areas(first = "  ")
        text_areas_multiple_page.submit()
        text_areas_multiple_page.should_have_error_message("This field is required.")
    except Exception as e:
        attach_screenshot(text_areas_multiple_page.page, "error_screenshot")
        raise e