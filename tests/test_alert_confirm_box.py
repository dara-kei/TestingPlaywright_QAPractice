from playwright.sync_api import Page, expect


def test_alert_confirm(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    # проверяем, что кнопка в наличии
    expect(page.locator("//a[@href='#']")).to_be_visible()

    # пишем функцию-слушателя до клика
    def hangle_dialog(dialog):
        assert dialog.type == "confirm" # проверяем тип
        assert "Select Ok or Cancel" in dialog.message # проверяем правильное сообщение на всплывающем окне
        dialog.accept() # нажать ок на всплывающем окне
    page.on("dialog", hangle_dialog)
    page.click("//a[@href='#']")
    expect(page.locator("#result-text")).to_have_text("Ok")


def test_alert_cancel(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    # Т.к. проверили уже тип алерта и сообщение на нем, можно вместо def функции написать lambda
    page.on("dialog", lambda dialog : dialog.dismiss()) # нажать cancel
    page.click("//a[@href='#']")
    expect(page.locator("#result-text")).to_have_text("Cancel")