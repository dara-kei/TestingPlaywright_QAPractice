import pytest

def test_areas_multiple_initial_state(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.should_have_default_state()


# positive tests
def test_submit_when_first_area_filled(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first = "Hello")
    text_areas_multiple_page.submit()
    text_areas_multiple_page.should_have_result_text("Hello")


@pytest.mark.parametrize("second, third", [("World", None), (None, "World")])
def test_submit_when_two_areas_filled(text_areas_multiple_page, second, third) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first="Hello", second = second, third = third)
    text_areas_multiple_page.submit()
    text_areas_multiple_page.should_have_result_text("HelloWorld")


def test_submit_when_all_areas_filled(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first = "Hello", second = "my", third = "World!")
    text_areas_multiple_page.submit()
    text_areas_multiple_page.should_have_result_text("HelloMyWorld!")


# negative tests

def test_submit_when_all_areas_empty(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.submit()
    text_areas_multiple_page.should_not_have_result()


def test_submit_when_required_area_not_filled(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(second = "my", third = "World")
    text_areas_multiple_page.submit()
    text_areas_multiple_page.should_not_have_result()

def test_submit_when_first_text_area_filled_with_only_spaces(text_areas_multiple_page) -> None:
    text_areas_multiple_page.open()
    text_areas_multiple_page.fill_areas(first = "  ")
    text_areas_multiple_page.submit()
    text_areas_multiple_page.should_have_error_message("This field is required.")