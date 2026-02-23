from playwright.sync_api import Page, expect


def test_iframe(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page") # проверяем, что iframe есть
    expect(page.locator("iframe")).to_have_count(1)
    new_page = page.frame_locator("iframe") # сначала надо зайти во frame
    expect(new_page.locator("h1")).to_have_text("Album example") # проверяем, что страница с контентом, а не с ошибкой 404
    new_page.locator('//span[@class="navbar-toggler-icon"]').click()


def test_modal(page: Page):
    page.goto("https://www.qa-practice.com/elements/popup/modal")
    expect(page.locator('#content > button')).to_have_text("Launch Pop-Up")
    page.locator('#content > button').click()
    page.locator('#id_checkbox_0').check()
    page.locator('//button[@type="submit"]').click()
    expect(page.locator("#result-text")).to_have_text("select me or not")

