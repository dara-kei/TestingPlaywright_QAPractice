
def test_page_have_click_button(alert_box_page) -> None:
    alert_box_page.open()
    alert_box_page.should_have_button_visible()


def test_alert_box_appear(alert_box_page) -> None:
    alert_box_page.open()
    alert_box_page.check_alert_dialog_and_accept("alert", "I am an alert!")

