def test_simple_button_click_shows_confirmation(simple_button_page) -> None:
    simple_button_page.open()
    simple_button_page.should_have_button_labeled("Click")
    simple_button_page.click()
    simple_button_page.should_have_result_text("Submitted")



