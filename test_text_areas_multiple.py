from playwright.sync_api import Page, expect
import pytest


URL = "https://www.qa-practice.com/elements/textarea/textareas"
FIRST_TEXT_AREA_LOCATOR = "#id_first_chapter"
SECOND_TEXT_AREA_LOCATOR = "#id_second_chapter"
THIRD_TEXT_AREA_LOCATOR = "#id_third_chapter"
BUTTON_LOCATOR= "#submit-id-submit"
RESULT_LOCATOR = "#result-text"

def test_areas_initial_state(page: Page) -> None:
    page.goto(URL)
    expect(page.locator("textarea")).to_have_count(3)
    expect(page.locator(f'label[for="{FIRST_TEXT_AREA_LOCATOR[1:]}"]')).to_have_text("First chapter*")
    expect(page.locator(f'label[for="{SECOND_TEXT_AREA_LOCATOR[1:]}"]')).to_have_text("Second chapter")
    expect(page.locator(f'label[for="{THIRD_TEXT_AREA_LOCATOR[1:]}"]')).to_have_text("Third chapter")
    expect(page.locator(FIRST_TEXT_AREA_LOCATOR)).to_have_attribute("required", "")


def test_filled_first_area(page: Page) -> None:
    page.goto(URL)
    page.locator(FIRST_TEXT_AREA_LOCATOR).fill("Hello")
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("Hello")


@pytest.mark.parametrize("other_area", [SECOND_TEXT_AREA_LOCATOR, THIRD_TEXT_AREA_LOCATOR])
def test_filled_two_areas(page: Page, other_area) -> None:
    page.goto(URL)
    page.locator(FIRST_TEXT_AREA_LOCATOR).fill("Hello")
    page.locator(other_area).fill("World!")
    page.locator(BUTTON_LOCATOR).click()
    # expect(page.locator(RESULT_LOCATOR)).to_have_text("HelloWorld!")
    expect(page.locator(RESULT_LOCATOR)).to_contain_text("Hello")
    expect(page.locator(RESULT_LOCATOR)).to_contain_text("World")

def test_filled_all_areas(page: Page) -> None:
    page.goto(URL)
    page.locator(FIRST_TEXT_AREA_LOCATOR).fill("Hello")
    page.locator(SECOND_TEXT_AREA_LOCATOR).fill("my")
    page.locator(THIRD_TEXT_AREA_LOCATOR).fill("World!")
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_contain_text("Hello")
    expect(page.locator(RESULT_LOCATOR)).to_contain_text("My")
    expect(page.locator(RESULT_LOCATOR)).to_contain_text("World!")


def test_empty_all_areas(page: Page) -> None:
    page.goto(URL)
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)


def test_not_filled_required_area(page: Page) -> None:
    page.goto(URL)
    page.locator(SECOND_TEXT_AREA_LOCATOR).fill("my")
    page.locator(THIRD_TEXT_AREA_LOCATOR).fill("World!")
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)