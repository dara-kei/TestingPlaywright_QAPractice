import pytest
import allure
from utils.allure_helper import attach_screenshot


@allure.feature("Multiple checkboxes")
@allure.title("Checking checkboxes page")
@allure.description("""
Requirements:
- There should be three checkboxes on the page.
- The label of the checkboxes should be:
- "One"
- "Two"
- "Three"
- The Submit button should always be enabled.
""")
def test_checkboxes_page_initial_state(checkboxes_multiple_page) -> None:
    try:
        checkboxes_multiple_page.open()
        checkboxes_multiple_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(checkboxes_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple checkboxes")
@allure.title("Checking submitting with one checkbox checked")
@allure.description("""
Requirements:
- After submitting the user should get the following result:
- if a checkbox has been selected, the name(s) of the selected checkbox(es) is(are) displayed to the user
""")
@pytest.mark.parametrize("checkbox_index, expected_result", [(0, "one"), (1, "two"), (2, "three")])
def test_one_checked_checkbox_shows_result(checkboxes_multiple_page, checkbox_index: int, expected_result: str) -> None:
    try:
        checkboxes_multiple_page.open()
        checkboxes_multiple_page.select_checkbox(checkbox_index)
        checkboxes_multiple_page.should_have_checkbox_checked(checkbox_index)
        checkboxes_multiple_page.submit()
        checkboxes_multiple_page.should_have_result_text(expected_result)
    except Exception as e:
        attach_screenshot(checkboxes_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple checkboxes")
@allure.title("Checking submitting with two checkboxes checked")
@allure.description("""
Requirements:
- After submitting the user should get the following result:
- if a checkbox has been selected, the name(s) of the selected checkbox(es) is(are) displayed to the user
""")
@pytest.mark.parametrize(
    "first_checkbox_index, second_checkbox_index, expected_result",
    [(0, 1, "one, two"), (1, 2, "two, three"), (0,2, "one, three")]
)
def test_two_checked_checkboxes_shows_result(
        checkboxes_multiple_page, first_checkbox_index: int, second_checkbox_index: int, expected_result: str) -> None:
    try:
        checkboxes_multiple_page.open()
        checkboxes_multiple_page.select_checkbox(first_checkbox_index)
        checkboxes_multiple_page.select_checkbox(second_checkbox_index)
        checkboxes_multiple_page.submit()
        checkboxes_multiple_page.should_have_result_text(expected_result)
    except Exception as e:
        attach_screenshot(checkboxes_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple checkboxes")
@allure.title("Checking submitting with all checkboxes checked")
@allure.description("""
Requirements:
- After submitting the user should get the following result:
- if a checkbox has been selected, the name(s) of the selected checkbox(es) is(are) displayed to the user
""")
def test_all_checked_checkboxes_shows_result(checkboxes_multiple_page) -> None:
    try:
        checkboxes_multiple_page.open()
        checkboxes_multiple_page.select_checkbox(0)
        checkboxes_multiple_page.select_checkbox(1)
        checkboxes_multiple_page.select_checkbox(2)
        checkboxes_multiple_page.submit()
        checkboxes_multiple_page.should_have_result_text("one, two, three")
    except Exception as e:
        attach_screenshot(checkboxes_multiple_page.page, "error_screenshot")
        raise e


@allure.feature("Multiple checkboxes")
@allure.title("Trying submitting no checkbox checked")
@allure.description("""
Requirements:
- After submitting the user should get the following result:
- if no checkbox was selected, then the result is not displayed
""")
def test_not_checked_checkboxes_not_show_result(checkboxes_multiple_page) -> None:
    try:
        checkboxes_multiple_page.open()
        checkboxes_multiple_page.submit()
        checkboxes_multiple_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(checkboxes_multiple_page.page, "error_screenshot")
        raise e
