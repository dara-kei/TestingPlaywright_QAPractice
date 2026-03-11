def test_button_is_disabled_by_default(disabled_button_page) -> None:
    disabled_button_page.open()
    disabled_button_page.should_have_disabled_button()

def test_button_state_can_be_changed_via_dropdown(disabled_button_page) -> None:
    disabled_button_page.open()
    disabled_button_page.choose_select_option("Enabled")
    disabled_button_page.should_have_enabled_button()
    disabled_button_page.choose_select_option("Disabled")
    disabled_button_page.should_have_disabled_button()

def test_button_click_shows_confirmation(disabled_button_page) -> None:
    disabled_button_page.open()
    disabled_button_page.choose_select_option("Enabled")
    disabled_button_page.click()
    disabled_button_page.should_have_result_text("Submitted")
