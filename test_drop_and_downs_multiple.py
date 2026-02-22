from playwright.sync_api import Page, expect
import pytest
import enum


URL = "https://www.qa-practice.com/elements/select/mult_select"
DROPDOWNS_LOCATORS = ["#id_choose_the_place_you_want_to_go",
                      "#id_choose_how_you_want_to_get_there",
                      "#id_choose_when_you_want_to_go"
                      ]
SUBMIT_BUTTON_LOCATOR = "#submit-id-submit"
RESULT_LOCATOR = "#result-text"


class Places(enum.Enum):
    SEA = "Sea"
    MOUNTAINS = "Mountains"
    OLD_TOWN = "Old town"
    OCEAN = "Ocean"
    RESTAURANT = "Restaurant"

class Transport(enum.Enum):
    CAR = "Car"
    BUS = "Bus"
    TRAIN = "Train"
    AIR = "Air"

class Date(enum.Enum):
    TODAY = "Today"
    TOMORROW = "Tomorrow"
    NEXT_WEEK = "Next week"


# Проверка обычного состояния: dropdowns три, они обязательные и имеют определенные названия
def test_initial_state(page: Page) -> None:
    page.goto(URL)
    expect(page.locator('//select[@class="select form-select"]')).to_have_count(3)
    expect(page.locator(f'label[for="{DROPDOWNS_LOCATORS[0][1:]}"]')).to_have_text("Choose the place you want to go*")
    expect(page.locator(f'label[for="{DROPDOWNS_LOCATORS[1][1:]}"]')).to_have_text("Choose how you want to get there*")
    expect(page.locator(f'label[for="{DROPDOWNS_LOCATORS[2][1:]}"]')).to_have_text("Choose when you want to go*")
    expect(page.locator(DROPDOWNS_LOCATORS[0])).to_have_attribute("required", "")
    expect(page.locator(DROPDOWNS_LOCATORS[1])).to_have_attribute("required", "")
    expect(page.locator(DROPDOWNS_LOCATORS[2])).to_have_attribute("required", "")


# Проверка, что все dropdown обязательные через не нажатие одного
@pytest.mark.parametrize(
    "dropdown_selected_1, text1, dropdown_selected_2, text2",
    [
        (DROPDOWNS_LOCATORS[1], "Car", DROPDOWNS_LOCATORS[2], "Today"),
        (DROPDOWNS_LOCATORS[0], "Sea", DROPDOWNS_LOCATORS[2], "Today"),
        (DROPDOWNS_LOCATORS[0], "Sea", DROPDOWNS_LOCATORS[1], "Car"),
    ]
)
def test_not_select_one_option(page: Page, dropdown_selected_1, text1, dropdown_selected_2, text2) -> None:
    page.goto(URL)
    page.locator(dropdown_selected_1).select_option(text1)
    page.locator(dropdown_selected_2).select_option(text2)
    page.locator(SUBMIT_BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)


# в этом тесте будут перебираться все комбинации (60 тестов!), что избыточно
# @pytest.mark.parametrize("first_dropdown", [x.value for x in Places])
# @pytest.mark.parametrize("second_dropdown", [x.value for x in Transport])
# @pytest.mark.parametrize("third_dropdown", [x.value for x in Date])
# def test_dropdowns(page: Page, first_dropdown, second_dropdown, third_dropdown) -> None:
#     page.goto(URL)
#     page.locator(DROPDOWNS_LOCATORS[0]).select_option(first_dropdown)
#     page.locator(DROPDOWNS_LOCATORS[1]).select_option(second_dropdown)
#     page.locator(DROPDOWNS_LOCATORS[2]).select_option(third_dropdown)
#     page.locator(SUBMIT_BUTTON_LOCATOR).click()
#     expect(page.locator(RESULT_LOCATOR)).to_have_text(f"to go by {second_dropdown.lower()} to the {first_dropdown.lower()} {third_dropdown.lower()}")


# проверка всех вариантов Places
@pytest.mark.parametrize("first_dropdown", [x.value for x in Places])
def test_each_place_option(page: Page, first_dropdown) -> None:
    page.goto(URL)
    page.locator(DROPDOWNS_LOCATORS[0]).select_option(first_dropdown)
    page.locator(DROPDOWNS_LOCATORS[1]).select_option("Car")
    page.locator(DROPDOWNS_LOCATORS[2]).select_option("Today")
    page.locator(SUBMIT_BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(f"to go by car to the {first_dropdown.lower()} today")


# проверка всех вариантов Transport
@pytest.mark.parametrize("second_dropdown", [x.value for x in Transport])
def test_each_transport_option(page: Page, second_dropdown) -> None:
    page.goto(URL)
    page.locator(DROPDOWNS_LOCATORS[0]).select_option("Mountains")
    page.locator(DROPDOWNS_LOCATORS[1]).select_option(second_dropdown)
    page.locator(DROPDOWNS_LOCATORS[2]).select_option("Tomorrow")
    page.locator(SUBMIT_BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(f"to go by {second_dropdown.lower()} to the mountains tomorrow")


# проверка оставшегося варианта Date
def test_left_date_option(page: Page) -> None:
    page.goto(URL)
    page.locator(DROPDOWNS_LOCATORS[0]).select_option("Old town")
    page.locator(DROPDOWNS_LOCATORS[1]).select_option("Train")
    page.locator(DROPDOWNS_LOCATORS[2]).select_option("Next week")
    page.locator(SUBMIT_BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text(f"to go by train to the old town next week")