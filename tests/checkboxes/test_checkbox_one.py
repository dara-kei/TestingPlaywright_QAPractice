
def test_checkbox_page_initial_state(checkbox_page) -> None:
    checkbox_page.open()
    checkbox_page.should_have_default_state()


def test_checked_checkbox_shows_result_after_submit(checkbox_page) -> None:
    checkbox_page.open()
    checkbox_page.select_checkbox()
    checkbox_page.should_have_checkbox_checked()
    checkbox_page.submit()
    checkbox_page.should_have_result_text("select me or not")


def test_unchecked_checkbox_not_show_result_after_submit(checkbox_page) -> None:
    checkbox_page.open()
    checkbox_page.submit()
    checkbox_page.should_not_have_result()
