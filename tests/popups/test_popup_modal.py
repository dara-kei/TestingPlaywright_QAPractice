
def test_name_of_button_that_open_popup(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.should_have_page_button_named("Launch Pop-Up")


def test_popup_initial_state(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.open_popup()
    popup_modal_page.should_have_popup()
    popup_modal_page.should_have_popup_default_state()


def test_send_popup_value_with_checkbox_checked(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.open_popup()
    popup_modal_page.submit_popup_with_checkbox_checked()
    popup_modal_page.should_have_result_text("select me or not")


def test_send_popup_value_with_checkbox_unchecked(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.open_popup()
    popup_modal_page.submit_popup_with_checkbox_unchecked()
    popup_modal_page.should_have_result_text("None")


def test_cancel_popup(popup_modal_page):
    popup_modal_page.open()
    popup_modal_page.open_popup()
    popup_modal_page.cancel_popup()
    popup_modal_page.should_not_have_result()

