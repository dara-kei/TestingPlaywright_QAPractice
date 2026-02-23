from playwright.sync_api import Page, expect
import re

URL = "https://www.qa-practice.com/elements/textarea/single"
TEXT_AREA_LOCATOR = "#id_text_area"
BUTTON_LOCATOR= "#submit-id-submit"
RESULT_LOCATOR = "#result-text"


def test_filled_text_area(page: Page) -> None:
    page.goto(URL)
    expect(page.locator(f'label[for="{TEXT_AREA_LOCATOR[1:]}"]')).to_have_text("Text area*")
    expect(page.locator(TEXT_AREA_LOCATOR)).to_have_attribute("required","") # проверяем, что это обязательное поле
    page.locator(TEXT_AREA_LOCATOR).fill("Hello!")
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("Hello!")


def test_empty_text_area(page: Page) -> None:
    page.goto(URL)
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)


def test_fill_text_area_with_only_spaces(page: Page) -> None:
    page.goto(URL)
    page.locator(TEXT_AREA_LOCATOR).fill("    ")
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator("#error_1_id_text_area")).to_have_text("This field is required.")
    expect(page.locator(TEXT_AREA_LOCATOR)).to_have_class(re.compile(".*is-invalid.*"))



