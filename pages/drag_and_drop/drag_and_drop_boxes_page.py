from playwright.sync_api import Page, expect
from pages.drag_and_drop.base_drag_and_drop_page import BaseDragAndDropPage


class DragAndDropBoxesPage(BaseDragAndDropPage):
    URL = "https://www.qa-practice.com/elements/dragndrop/boxes"
    def __init__(self, page : Page) -> None:
        super().__init__(page)
        self.droppable = page.locator("#rect-droppable")
        self.draggable = page.locator("#rect-draggable")
        self.text = page.locator("#text-droppable")

    def should_have_default_state(self):
        self.should_be_visible(self.droppable)
        self.should_be_visible(self.draggable)

    def drag_box_to_target(self):
        self.drag_and_drop(self.draggable, self.droppable)

    def should_be_dropped_successfully(self):
        self.should_have_result_text(self.text, "Dropped!")

    def draggable_should_be_inside_droppable(self):
        expect(self.droppable.locator("#rect-draggable")).to_be_visible()


