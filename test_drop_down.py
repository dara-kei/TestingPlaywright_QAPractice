from playwright.sync_api import Page, expect
import pytest
from pages.drop_down_page import DropDownPage, ProgrammingLanguage


@pytest.mark.parametrize("choice", [x.value for x in ProgrammingLanguage]) # для каждого элемента в ProgLanguage вернет его value
def test_select_options(select_page, choice) -> None:
    select_page.open_url()
    select_page.select_language(choice)
    select_page.submit()
    select_page.check_result(choice)


def test_select_no_options(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    page.locator("#submit-id-submit").click()
    expect(page.locator("#result-text")).to_have_count(0)

def test_select_is_required_field(page:Page) -> None:
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    expect(page.locator("#id_choose_language")).to_have_attribute("required", "")

def test_field_name(page:Page) -> None:
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    expect(page.locator("label[for='id_choose_language']")).to_have_text("Choose language*")