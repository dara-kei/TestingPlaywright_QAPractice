import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Single checkbox")
@allure.title("Checking checkbox page")
@allure.description("""
Requirements:
- There should be one checkbox on the page.
- The label of the checkbox should be "Select me or not"
- The user should be able to select the checkbox
- The Submit button should always be enabled
""")
def test_checkbox_page_initial_state(checkbox_page) -> None:
    try:
        checkbox_page.open()
        checkbox_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(checkbox_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Single checkbox")
@allure.title("Checking checkbox submit")
@allure.description("""
Requirements:
- After submitting the user should get the following result:
- if a checkbox has been selected, the name of the selected checkbox is displayed to the user
""")
def test_checked_checkbox_shows_result_after_submit(checkbox_page) -> None:
    try:
        checkbox_page.open()
        checkbox_page.select_checkbox()
        checkbox_page.should_have_checkbox_checked()
        checkbox_page.submit()
        checkbox_page.should_have_result_text("select me or not")
    except Exception as e:
        attach_screenshot(checkbox_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
@allure.feature("Single checkbox")
@allure.title("Trying submitting with unchecked checkbox")
@allure.description("""
Requirements:
- After submitting the user should get the following result:
- if the checkbox was not selected, then the result is not displayed
""")
def test_unchecked_checkbox_not_show_result_after_submit(checkbox_page) -> None:
    try:
        checkbox_page.open()
        checkbox_page.submit()
        checkbox_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(checkbox_page.page, "error_screenshot")
        raise e
