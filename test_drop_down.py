import pytest
from pages.drop_down_page import ProgrammingLanguage


@pytest.mark.parametrize("choice", [x.value for x in ProgrammingLanguage]) # для каждого элемента в ProgLanguage вернет его value
def test_select_options(select_page, choice) -> None:
    select_page.open_url()
    select_page.select_language(choice)
    select_page.submit()
    select_page.result_should_have_text(choice)


def test_select_no_options(select_page) -> None:
    select_page.open_url()
    select_page.submit()
    select_page.result_should_not_exist()

def test_select_is_required_field(select_page) -> None:
    select_page.open_url()
    select_page.field_should_be_required()

def test_field_name(select_page) -> None:
    select_page.open_url()
    select_page.should_have_field_name()