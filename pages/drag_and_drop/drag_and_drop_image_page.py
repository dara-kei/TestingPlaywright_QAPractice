from playwright.sync_api import Page, expect
from pages.drag_and_drop.base_drag_and_drop_page import BaseDragAndDropPage


class DragAndDropImagePage(BaseDragAndDropPage):
    URL = "https://www.qa-practice.com/elements/dragndrop/images"
    def __init__(self, page : Page) -> None:
        super().__init__(page)
        self.droppable_boxes = { "top": page.locator("#rect-droppable1"), "bottom" : page.locator("#rect-droppable2")}
        self.img = page.locator("img[src='/static/home/smile.png']")

    def should_have_default_state(self):
        self.should_be_counted(self.page.locator(".rect-droppable"), 2)
        self.should_be_visible(self.droppable_boxes["bottom"])
        self.should_be_visible(self.droppable_boxes["top"])
        self.should_be_visible(self.droppable_boxes["bottom"].locator("img"))
        self.should_be_counted(self.page.locator("#rect-droppable2 img"),0)

    def drag_image_to_box(self, droppable_box):
        self.drag_and_drop(self.img, self.droppable_boxes[droppable_box])

    def should_be_dropped_successfully(self, droppable_box):
        self.should_have_result_text(self.droppable_boxes[droppable_box], "Dropped!")


    def should_have_image_inside_box(self, droppable_box):
        expect(self.droppable_boxes[droppable_box].locator("img")).to_be_visible()


    def should_have_empty_box(self, droppable_box):
        self.should_not_be_visible(self.droppable_boxes[droppable_box].locator("img"))
