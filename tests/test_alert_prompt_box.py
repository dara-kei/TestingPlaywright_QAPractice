from playwright.sync_api import Page, expect


def test_alert_prompt(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/alert/prompt")
    # проверяем, что кнопка в наличии
    expect(page.locator("//a[@href='#']")).to_be_visible()

    # пишем функцию-слушателя до клика
    def hangle_dialog(dialog):
        assert dialog.type == "prompt" # проверяем тип
        assert "Please enter some text" in dialog.message # проверяем правильное сообщение на всплывающем окне
        dialog.accept("Hello!") # вводим текст и нажимаем ок
    page.on("dialog", hangle_dialog)
    page.click("//a[@href='#']")
    expect(page.locator("#result-text")).to_have_text("Hello!")


def test_alert_prompt_cancel(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/alert/prompt")
    page.on("dialog", lambda dialog : dialog.dismiss()) # нажать cancel
    page.click("//a[@href='#']")
    expect(page.locator("#result-text")).to_have_text("You canceled the prompt")