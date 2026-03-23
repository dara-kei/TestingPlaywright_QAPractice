import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Iframe")
@allure.title("Checking iframe with a sample page")
@allure.description("""
Requirements:
- There should be an iframe with a sample page.
""")
def test_iframe_with_sample_page(iframe_page):
    try:
        iframe_page.open()
        iframe_page.should_have_iframe()
        iframe_page.should_not_have_empty_iframe()
    except Exception as e:
        attach_screenshot(iframe_page.page, "error_screenshot")
        raise e

