from playwright.sync_api import Page, expect


# тестирую кнопки на нескольких страницах, поэтому не выносила в отдельные переменные


def test_simple_button(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/button/simple")
    expect(page.locator("#submit-id-submit")).to_have_value("Click")
    page.locator("#submit-id-submit").click()
    expect(page.locator("#result-text")).to_have_text("Submitted")


def test_disabled_button(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/button/disabled")
    expect(page.locator("#submit-id-submit")).to_have_value("Submit")
    expect(page.locator("#submit-id-submit")).to_be_disabled()


def test_enable_button(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/button/disabled")
    page.locator("#id_select_state").select_option("Enabled")
    expect(page.locator("#submit-id-submit")).to_be_enabled()
    page.locator("#id_select_state").select_option("Disabled")
    expect(page.locator("#submit-id-submit")).to_be_disabled()
    page.locator("#id_select_state").select_option("Enabled")
    page.locator("#submit-id-submit").click()
    expect(page.locator("#result-text")).to_have_text("Submitted")
