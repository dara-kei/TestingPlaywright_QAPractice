from playwright.sync_api import Page, expect


def test_modal_popup_send(page: Page):
    page.goto("https://www.qa-practice.com/elements/popup/modal")
    expect(page.locator("#content > button")).to_have_text("Launch Pop-Up")
    page.locator("#content > button").click()
    popup = page.locator("#exampleModal")
    expect(popup).to_be_visible()
    expect(popup.locator("#exampleModalLabel")).to_have_text("I am a Pop-Up")
    expect(popup.locator('label[for="id_checkbox_0"]')).to_have_text("Select me or not")
    expect(popup.locator(".modal-footer button")).to_have_count(2)
    expect(popup.locator(".modal-footer button[type='button']")).to_have_text("Close") # не соответствие требованиям: There should be two buttons: "Cancel" and "Send"
    expect(popup.locator(".modal-footer button[type='submit']")).to_have_text("Send")
    popup.locator("#id_checkbox_0").check()
    popup.locator('button[type="submit"]').click()
    expect(page.locator("#result-text")).to_have_text("select me or not")


def test_modal_popup_send_without_checkbox_checked(page: Page):
    page.goto("https://www.qa-practice.com/elements/popup/modal")
    page.locator("#content > button").click()
    popup = page.locator("#exampleModal")
    popup.locator('button[type="submit"]').click()
    expect(page.locator("#result-text")).to_have_text("None")


def test_modal_popup_close(page: Page):
    page.goto("https://www.qa-practice.com/elements/popup/modal")
    page.locator("#content > button").click()
    popup = page.locator("#exampleModal")
    popup.locator(".modal-footer button[type='button']").click()
    expect(page.locator("#result-text")).to_have_count(0)







def test_modal_popup_classwork(page: Page):
    page.goto("https://www.qa-practice.com/elements/popup/modal")
    page.locator("#content > button").click()
    popup = page.locator('#content') # область не поп-апа а общая
    checkbox = page.locator('#id_checkbox_0')
    checkbox.check()
    button = popup.locator('//button[@type="submit"]')
    button.click()
    expect(page.locator("#result-text")).to_have_text("select me or not")




