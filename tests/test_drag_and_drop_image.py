from playwright.sync_api import Page, expect





def test_initial_state(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/dragndrop/images")
    expect(page.locator(".rect-droppable")).to_have_count(2) # Проверяем, что квадрата 2
    expect(page.locator("#rect-droppable1")).to_be_visible()
    expect(page.locator("#rect-droppable2")).to_be_visible()
    expect(page.locator("#rect-droppable1 img")).to_be_visible() # XPath "//div[@id='rect-droppable1']//img"
    expect(page.locator("#rect-droppable2 img")).to_have_count(0)


def test_smile_drop(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/dragndrop/images")
    for _ in range(3):
        page.locator("#rect-droppable1 img").drag_to(page.locator("#rect-droppable2"))
        expect(page.locator("#rect-droppable2 img")).to_be_visible()
        expect(page.locator("#rect-droppable2")).to_have_text("Dropped!")
        expect(page.locator("#rect-droppable1 img")).not_to_be_visible()

        page.locator("#rect-droppable2 img").drag_to(page.locator("#rect-droppable1"))
        expect(page.locator("#rect-droppable1 img")).to_be_visible()
        expect(page.locator("#rect-droppable1")).to_have_text("Dropped!")
        expect(page.locator("#rect-droppable2 img")).not_to_be_visible()

