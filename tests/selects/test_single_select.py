import pytest
from models.programming_language import ProgrammingLanguage


def test_single_select_page_initial_state(single_select_page) -> None:
    single_select_page.open()
    single_select_page.should_have_default_state()


@pytest.mark.parametrize("language_option", [lang.value for lang in ProgrammingLanguage]) # для каждого элемента в ProgLanguage вернет его value
def test_user_can_select_options(single_select_page, language_option) -> None:
    single_select_page.open()
    single_select_page.choose_select_option(language_option)
    single_select_page.submit()
    single_select_page.should_have_result_text(language_option)


def test_submit_without_selection_shows_no_result(single_select_page) -> None:
    single_select_page.open()
    single_select_page.submit()
    single_select_page.should_not_have_result()


