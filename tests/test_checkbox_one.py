def test_checkbox_page_initial_state(checkbox_page) -> None:
    checkbox_page.open_page()
    checkbox_page.checkbox_should_be_visible()
    checkbox_page.checkbox_should_exist()
    checkbox_page.checkbox_should_have_text("Select me or not")
    checkbox_page.select_checkbox()
    checkbox_page.checkbox_should_be_checked()
    checkbox_page.button_should_have_name("Submit")
    checkbox_page.button_should_be_enable()


def test_checkbox_checked(checkbox_page) -> None:
    checkbox_page.open_page()
    checkbox_page.select_checkbox()
    checkbox_page.submit()
    checkbox_page.result_should_have_text("select me or not")


def test_checkbox_not_checked(checkbox_page) -> None:
    checkbox_page.open_page()
    checkbox_page.submit()
    checkbox_page.result_should_not_exist()
