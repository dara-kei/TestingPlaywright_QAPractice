def test_page_have_click_button(alert_confirmation_box_page) -> None:
    alert_confirmation_box_page.open()
    alert_confirmation_box_page.should_have_button_visible()


def test_confirm_dialog_info_and_accept(alert_confirmation_box_page) -> None:
    alert_confirmation_box_page.open()
    alert_confirmation_box_page.check_alert_dialog_and_accept("confirm", "Select Ok or Cancel")
    alert_confirmation_box_page.should_have_result_text("Ok")
# БАГ! Alert window should display text "I am an alert!"


def test_confirm_dialog_cancel(alert_confirmation_box_page) -> None:
    alert_confirmation_box_page.open()
    alert_confirmation_box_page.alert_dialog_dismiss()
    alert_confirmation_box_page.should_have_result_text("Cancel")

