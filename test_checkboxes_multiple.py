import pytest
from playwright.sync_api import Page, expect


URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"
BUTTON_LOCATOR = "#submit-id-submit"
RESULT_LOCATOR = "#result"
CHECKBOXES = [
    "#id_checkboxes_0",
    "#id_checkboxes_1",
    "#id_checkboxes_2"
]

def test_checkboxes_page_initial_state(page: Page) -> None:
    page.goto(URL)
    expect(page.locator('input[type = "checkbox"]')).to_have_count(3) # проверяем, что на странице 3 чекбокса
    expect(page.locator('label[for = "id_checkboxes_0"]')).to_have_text("One") # проверяем названия чекбоксов
    expect(page.locator('label[for = "id_checkboxes_1"]')).to_have_text("Two")
    expect(page.locator('label[for = "id_checkboxes_2"]')).to_have_text("Three")
    expect(page.locator(BUTTON_LOCATOR)).to_have_value("Submit")
    expect(page.locator(BUTTON_LOCATOR)).to_be_enabled() # проверяем, что кнопка активна


def test_checkboxes_not_checked(page: Page) -> None:
    page.goto(URL)
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)


@pytest.mark.parametrize(
    "checkbox, expected_result",
    [
        (CHECKBOXES[0], "Selected checkboxes:\none"),
        (CHECKBOXES[1], "Selected checkboxes:\ntwo"),
        (CHECKBOXES[2], "Selected checkboxes:\nthree")
    ]
)
def test_checkboxes(page: Page, checkbox: str, expected_result: str) -> None:
    page.goto(URL)
    expect(page.locator(checkbox)).to_be_visible()
    page.locator(checkbox).check()
    expect(page.locator(checkbox)).to_be_checked() # чекбокс нажат
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(expected_result)


@pytest.mark.parametrize(
    "first_checkbox, second_checkbox, expected_result",
    [
        (CHECKBOXES[0], CHECKBOXES[1], "Selected checkboxes:\none, two"),
        (CHECKBOXES[1], CHECKBOXES[2], "Selected checkboxes:\ntwo, three"),
        (CHECKBOXES[0], CHECKBOXES[2], "Selected checkboxes:\none, three")
    ]
)
def test_two_checkboxes_checked(page: Page, first_checkbox: str, second_checkbox: str, expected_result: str) -> None:
    page.goto(URL)
    page.locator(first_checkbox).check()
    page.locator(second_checkbox).check()
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(expected_result)


def test_all_checkboxes_checked(page: Page) -> None:
    page.goto(URL)
    page.locator(CHECKBOXES[0]).check()
    page.locator(CHECKBOXES[1]).check()
    page.locator(CHECKBOXES[2]).check()
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("Selected checkboxes:\none, two, three")
