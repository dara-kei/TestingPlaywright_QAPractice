from playwright.sync_api import Page, expect
import pytest
import helper
import re


URL = "https://www.qa-practice.com/elements/input/passwd"
PASSWD_INPUT_LOCATOR = '//input[@id="id_password"]'
RESULT_LOCATOR = '//p[@class="result-text"]'
ERROR_MESSAGE_LOCATOR = '//span[@id="error_1_id_password"]'


@pytest.mark.parametrize("text", ["Tested1#", "Tested1#привет", "&&&&!%$@Tested66789"])
def test_valid_passwd(page: Page, text) -> None:
    helper.submit(page, URL, PASSWD_INPUT_LOCATOR, text)
    expect(page.locator(RESULT_LOCATOR)).to_be_visible()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(text)


@pytest.mark.parametrize("text", ["tested1#", "Tested11", "Tested##", "Test1#"])
def test_invalid_passwd(page: Page, text) -> None:
    helper.submit(page, URL, PASSWD_INPUT_LOCATOR, text)
    expect(page.locator(PASSWD_INPUT_LOCATOR)).to_have_class(re.compile(".*is-invalid.*"))
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text("Low password complexity")


def test_empty_passwd(page: Page) -> None:
    helper.submit(page, URL, PASSWD_INPUT_LOCATOR, "")
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)


def test_passwd_with_only_spaces(page: Page) -> None:
    helper.submit(page, URL, PASSWD_INPUT_LOCATOR, "  ")
    expect(page.locator(PASSWD_INPUT_LOCATOR)).to_have_class(re.compile(".*is-invalid.*"))
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text("This field is required.")


