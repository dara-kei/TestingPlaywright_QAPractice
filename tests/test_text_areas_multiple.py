import pytest

def test_areas_initial_state(text_areas_page):
    text_areas_page.open_url()
    text_areas_page.page_should_have_three_text_areas()
    text_areas_page.areas_should_have_correct_labels()
    text_areas_page.first_area_should_be_required()


def test_filled_first_area(text_areas_page):
    text_areas_page.open_url()
    text_areas_page.fill_areas(first = "Hello")
    text_areas_page.submit()
    text_areas_page.result_should_have_text("Hello")


@pytest.mark.parametrize(
    "second, third",
    [
        ("World", None),
        (None, "World")

    ]
)
def test_filled_two_areas(text_areas_page, second, third) -> None:
    text_areas_page.open_url()
    text_areas_page.fill_areas(first="Hello", second = second, third = third)
    text_areas_page.submit()
    text_areas_page.result_should_have_text("HelloWorld")

def test_filled_all_areas(text_areas_page):
    text_areas_page.open_url()
    text_areas_page.fill_areas(first = "Hello", second = "my", third = "World!")
    text_areas_page.submit()
    text_areas_page.result_should_have_text("HelloMyWorld!")

def test_empty_all_areas(text_areas_page):
    text_areas_page.open_url()
    text_areas_page.submit()
    text_areas_page.result_should_not_exist()

def test_not_filled_required_area(text_areas_page):
    text_areas_page.open_url()
    text_areas_page.fill_areas(second = "my", third = "World")
    text_areas_page.submit()
    text_areas_page.result_should_not_exist()

