from playwright.sync_api import Page, expect


def test_initial_state(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    expect(page.locator("#rect-droppable")).to_be_visible()
    expect(page.locator("#rect-draggable")).to_be_visible()


def test_drag_and_drop(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    source = page.locator("#rect-draggable") # элемент, который переносим
    target = page.locator("#rect-droppable") # куда переносим
    source.drag_to(target) # переносим элемент
    expect(page.locator("#text-droppable")).to_have_text("Dropped!")
    # проверяем, что второй drag ничего не меняет
    source.drag_to(target)
    expect(page.locator("#text-droppable")).to_have_text("Dropped!")


def test_drag_and_drop_by_hands(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    source = page.locator("#rect-draggable")
    target = page.locator("#rect-droppable")
    source.hover() # наводим курсов на источник
    page.mouse.down() # нажимаем мышкой
    target.hover() # наводим на цель перетаскивания
    # target.hover() иногда надо дважды
    page.mouse.up()
