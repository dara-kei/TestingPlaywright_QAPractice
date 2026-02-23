from playwright.sync_api import Page, expect


def test_new_tab_opens_correctly_by_link(context):
    # 1. Открываем первую страницу
    page = context.new_page()
    page.goto("https://www.qa-practice.com/elements/new_tab/link")

    # 2. Ожидаем появление новой вкладки при клике
    with context.expect_page() as new_page_info:
        page.locator("#new-page-link").click()

    # 3. Получаем объект новой вкладки
    new_tab = new_page_info.value

    # 4. Ждём полной загрузки новой страницы
    new_tab.wait_for_load_state()

    # 5. Проверяем URL новой вкладки
    expect(new_tab).to_have_url("https://www.qa-practice.com/elements/new_tab/new_page")

    # 6. Проверяем содержимое новой вкладки
    expect(new_tab.locator("#result-text")).to_have_text("I am a new page in a new tab")

    # 7. Проверяем, что исходная вкладка осталась прежней
    expect(page).to_have_url("https://www.qa-practice.com/elements/new_tab/link")



def test_new_tab_opens_correctly_by_button(context):
    page = context.new_page()
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    with context.expect_page() as new_page_info:
        page.locator("#new-page-button").click()
    new_tab = new_page_info.value
    expect(new_tab).to_have_url("https://www.qa-practice.com/elements/new_tab/new_page")
    expect(new_tab.locator("#result-text")).to_have_text("I am a new page in a new tab")
    expect(page).to_have_url("https://www.qa-practice.com/elements/new_tab/button")