from playwright.sync_api import Page, expect


def test_alert_button(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/alert/alert")
    # проверяем, что кнопка в наличии
    expect(page.locator(".a-button")).to_be_visible()

    # пишем функцию-слушателя до клика
    def hangle_dialog(dialog):
        assert dialog.type == "alert" # проверяем, что тип alert
        assert "I am an alert!" in dialog.message # проверяем правильное сообщение на всплывающем окне
        dialog.accept() # нажать ок на всплывающем окне
    page.on("dialog", hangle_dialog)
    page.click(".a-button")
