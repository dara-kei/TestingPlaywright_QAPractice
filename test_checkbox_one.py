from playwright.sync_api import Page, expect

URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
CHECKBOX_LOCATOR = "#id_checkbox_0"
BUTTON_LOCATOR = "#submit-id-submit"
RESULT_LOCATOR = "#result"

def test_checkbox_page_initial_state(page: Page) -> None:
    page.goto(URL)
    expect(page.locator(CHECKBOX_LOCATOR)).to_be_visible()
    expect(page.locator("input[type = checkbox]")).to_have_count(1)
    expect(page.locator('label[for="id_checkbox_0"]')).to_have_text("Select me or not")
    page.locator(CHECKBOX_LOCATOR).check()
    expect(page.locator(CHECKBOX_LOCATOR)).to_be_checked()
    expect(page.locator(BUTTON_LOCATOR)).to_have_value("Submit")
    expect(page.locator(BUTTON_LOCATOR)).to_be_enabled()


def test_checkbox_checked(page: Page) -> None:
    page.goto(URL)
    page.locator(CHECKBOX_LOCATOR).check()
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_text("Selected checkboxes:\nselect me or not")


def test_checkbox_not_checked(page: Page) -> None:
    page.goto(URL)
    page.locator(BUTTON_LOCATOR).click()
    expect(page.locator(RESULT_LOCATOR)).to_have_count(0)
