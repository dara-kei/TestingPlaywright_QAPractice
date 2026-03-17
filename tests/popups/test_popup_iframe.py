import pytest


def test_name_of_button_that_open_popup(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.should_have_button_open_popup_named("Launch Pop-Up")


def test_popup_initial_state(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_popup()
    popup_iframe_page.should_have_popup_default_state()


def test_input_form_initial_state(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_popup()
    popup_iframe_page.click_check()
    popup_iframe_page.should_have_input_form_default_state()


def test_submit_input_form_with_valid_data(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_popup()
    text = popup_iframe_page.get_iframe_text()
    popup_iframe_page.click_check()
    popup_iframe_page.fill_input_form(text)
    popup_iframe_page.submit_input_form()
    popup_iframe_page.should_have_result_text("Correct!")


@pytest.mark.parametrize("invalid_data", ["  ", "hglhhkjnk", "*"])
def test_submit_input_form_with_invalid_data(popup_iframe_page, invalid_data):
    popup_iframe_page.open()
    popup_iframe_page.open_popup()
    popup_iframe_page.click_check()
    popup_iframe_page.fill_input_form(invalid_data)
    popup_iframe_page.submit_input_form()
    popup_iframe_page.should_have_result_text("Nope. Better luck next time!")


def test_cancel_iframe_popup(popup_iframe_page):
    popup_iframe_page.open()
    popup_iframe_page.open_popup()
    popup_iframe_page.click_close()
    popup_iframe_page.should_not_have_result()
