from playwright.sync_api import Page, expect
import pytest
import helper
import re


URL = "https://www.qa-practice.com/elements/input/email"
EMAIL_INPUT_LOCATOR = '//input[@id="id_email"]'
RESULT_LOCATOR = '//p[@class="result-text"]'
ERROR_MESSAGE_LOCATOR = '//span[@class="invalid-feedback"]'


@pytest.mark.parametrize("text", ["user@google.com", "user@localhost", " user@localhost "])
def test_valid_email(page: Page, text) -> None:
    helper.submit(page, URL, EMAIL_INPUT_LOCATOR, text)
    expect(page.locator(RESULT_LOCATOR)).to_be_visible()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(text)


def test_empty_email_field(page: Page) -> None:
    helper.submit(page, URL, EMAIL_INPUT_LOCATOR, "")
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)
# на странице ничего не происходит, запрос блокируется браузером, появляется сообщение "Please fill out this field"
# поэтому проверяем, что "#result-text" было 0 раз


def test_invalid_email(page: Page) -> None:
    helper.submit(page, URL, EMAIL_INPUT_LOCATOR, "userlocalhost")
    expect(page.locator(EMAIL_INPUT_LOCATOR)).to_have_class(re.compile(".*is-invalid.*"))
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text("Enter a valid email address.")


def test_email_with_non_latin_characters(page: Page) -> None:
    helper.submit(page, URL, EMAIL_INPUT_LOCATOR, "юсер@localhost")
    expect(page.locator(EMAIL_INPUT_LOCATOR)).to_have_class(re.compile(".*is-invalid.*"))
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text("Enter a valid email address.")


def test_invalid_email_with_only_spaces(page: Page) -> None:
    helper.submit(page, URL, EMAIL_INPUT_LOCATOR, "  ")
    expect(page.locator(EMAIL_INPUT_LOCATOR)).to_have_class(re.compile(".*is-invalid.*"))
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text("This field is required.")

