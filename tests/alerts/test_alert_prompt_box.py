def test_page_have_click_button(alert_prompt_box_page) -> None:
    alert_prompt_box_page.open()
    alert_prompt_box_page.should_have_button_visible()


def test_prompt_dialog_info_and_accept(alert_prompt_box_page) -> None:
    alert_prompt_box_page.open()
    alert_prompt_box_page.check_alert_dialog_and_accept("prompt", "Please enter some text", prompt_text= "Hello!")
    alert_prompt_box_page.should_have_result_text("Hello!")
# БАГ! Alert window should display text "I am an alert!"


def test_prompt_dialog_cancel(alert_prompt_box_page) -> None:
    alert_prompt_box_page.open()
    alert_prompt_box_page.alert_dialog_dismiss()
    alert_prompt_box_page.should_have_result_text("You canceled the prompt")


