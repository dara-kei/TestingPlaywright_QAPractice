import pytest
from data.programming_language import ProgrammingLanguage
import allure
from utils.allure_helper import attach_screenshot


@allure.feature("Single select")
@allure.title("Checking select default state")
@allure.description("""
Requirements:
- Field name is "Choose language".
- This is a required field.
""")
def test_single_select_page_initial_state(single_select_page) -> None:
    try:
        single_select_page.open()
        single_select_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(single_select_page.page, "error_screenshot")
        raise e


@allure.feature("Single select")
@allure.title("Checking submitting select")
@allure.description("""
Requirements:
- User should be able to select any option.
- The result can be sent using the Submit button.
- After submitting the form, the option selected by the user is displayed on the page.
""")
@pytest.mark.parametrize("language_option", [lang.value for lang in ProgrammingLanguage]) # для каждого элемента в ProgLanguage вернет его value
def test_submit_with_select_selected(single_select_page, language_option) -> None:
    try:
        single_select_page.open()
        single_select_page.choose_select_option(language_option)
        single_select_page.submit()
        single_select_page.should_have_result_text(language_option)
    except Exception as e:
        attach_screenshot(single_select_page.page, "error_screenshot")
        raise e


@allure.feature("Single select")
@allure.title("Trying submitting with select not selected")
@allure.description("""
Requirements:
- This is a required field
""")
def test_submit_without_selection_shows_no_result(single_select_page) -> None:
    try:
        single_select_page.open()
        single_select_page.submit()
        single_select_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(single_select_page.page, "error_screenshot")
        raise e


