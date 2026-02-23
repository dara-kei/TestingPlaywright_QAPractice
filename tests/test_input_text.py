from playwright.sync_api import Page, expect
import re
import helper

URL = "https://www.qa-practice.com/elements/input/simple"
INPUT_LOCATOR = '//input[@id="id_text_string"]'                       # CSS: "input#id_text_string"
RESULT_LOCATOR = '//p[@class="result-text"]'                          # CSS:  "p#result-text"
ERROR_MESSAGE_LOCATOR = '//span[@id="error_1_id_text_string"]'        # CSS: "span#error_1_id_text_string"

# так изначально выглядели все функции:
# def test_filled_with_2_letters(page: Page) -> None:
#     page.goto("https://www.qa-practice.com/elements/input/simple")
#     page.locator("#id_text_string").click()
#     page.locator("#id_text_string").fill("hh")
#     page.locator("#id_text_string").press("Enter")
#     expect(page.locator("#result-text")).to_be_visible()
#     expect(page.locator("#result-text")).to_have_text("hh")
# создала в helper def submit, которая содержит действия, а url, локаторы вынесла сверху этого файла

def test_input_with_2_letters(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR,"hh")
    expect(page.locator(RESULT_LOCATOR)).to_be_visible()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("hh")


def test_input_with_valid_letters(page: Page ) -> None:
    helper.submit(page, URL, INPUT_LOCATOR,"Fgh77_-")
    expect(page.locator(RESULT_LOCATOR)).to_be_visible()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("Fgh77_-")

def test_input_with_25_letters(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "1234567890123456789012345")
    expect(page.locator(RESULT_LOCATOR)).to_be_visible()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("1234567890123456789012345")


def test_empty_field(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "")
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)

    # message = page.locator(INPUT_LOCATOR).evaluate("el =>
    # дополнить по презентацию


def test_input_with_less_letters(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "h")
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text('Please enter 2 or more characters')
    expect(page.locator(INPUT_LOCATOR)).to_have_class(re.compile('.*is-invalid.*'))
    # то же что и предыдущая строка:
    # expect(page.locator("#id_text_string.is-invalid")).to_be_visible()


def test_input_with_more_letters(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "12345678901234567890123456")
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text('Please enter no more than 25 characters')
    expect(page.locator(INPUT_LOCATOR)).to_have_class(re.compile('.*is-invalid.*'))


def test_input_with_non_latin_characters(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "привет")
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text('Enter a valid string consisting of letters, numbers, underscores or hyphens.')
    expect(page.locator(INPUT_LOCATOR)).to_have_class(re.compile('.*is-invalid.*'))


def test_input_with_invalid_let(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "@@")
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text('Enter a valid string consisting of letters, numbers, underscores or hyphens.')
    expect(page.locator(INPUT_LOCATOR)).to_have_class(re.compile('.*is-invalid.*'))


def test_input_with_space(page: Page) -> None:
    helper.submit(page, URL, INPUT_LOCATOR, "  ")
    expect(page.locator(ERROR_MESSAGE_LOCATOR)).to_have_text('This field is required.')
    expect(page.locator(INPUT_LOCATOR)).to_have_class(re.compile('.*is-invalid.*'))

