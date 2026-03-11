def test_looks_like_a_button_click_shows_confirmation(looks_like_button_page) -> None:
    looks_like_button_page.open()
    looks_like_button_page.should_have_button_labeled("Click")
    looks_like_button_page.click()
    looks_like_button_page.should_have_result_text("Submitted")