import pytest


def test_checkboxes_page_initial_state(checkboxes_multiple_page) -> None:
    checkboxes_multiple_page.open()
    checkboxes_multiple_page.should_have_default_state()


@pytest.mark.parametrize("checkbox_index, expected_result", [(0, "one"), (1, "two"), (2, "three")])
def test_one_checked_checkbox_shows_result(checkboxes_multiple_page, checkbox_index: int, expected_result: str) -> None:
    checkboxes_multiple_page.open()
    checkboxes_multiple_page.select_checkbox(checkbox_index)
    checkboxes_multiple_page.should_have_checkbox_checked(checkbox_index)
    checkboxes_multiple_page.submit()
    checkboxes_multiple_page.should_have_result_text(expected_result)


@pytest.mark.parametrize(
    "first_checkbox_index, second_checkbox_index, expected_result",
    [(0, 1, "one, two"), (1, 2, "two, three"), (0,2, "one, three")]
)
def test_two_checked_checkboxes_shows_result(
        checkboxes_multiple_page, first_checkbox_index: int, second_checkbox_index: int, expected_result: str) -> None:
    checkboxes_multiple_page.open()
    checkboxes_multiple_page.select_checkbox(first_checkbox_index)
    checkboxes_multiple_page.select_checkbox(second_checkbox_index)
    checkboxes_multiple_page.submit()
    checkboxes_multiple_page.should_have_result_text(expected_result)


def test_all_checked_checkboxes_shows_result(checkboxes_multiple_page) -> None:
    checkboxes_multiple_page.open()
    checkboxes_multiple_page.select_checkbox(0)
    checkboxes_multiple_page.select_checkbox(1)
    checkboxes_multiple_page.select_checkbox(2)
    checkboxes_multiple_page.submit()
    checkboxes_multiple_page.should_have_result_text("one, two, three")


def test_not_checked_checkboxes_not_show_result(checkboxes_multiple_page) -> None:
    checkboxes_multiple_page.open()
    checkboxes_multiple_page.submit()
    checkboxes_multiple_page.should_not_have_result()
