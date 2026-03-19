from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class DragAndDropBoxesPage(BasePage):
    URL = "https://www.qa-practice.com/elements/dragndrop/boxes"
    def __init__(self, page : Page) -> None:
        super().__init__(page)
        self.droppable = page.locator("#rect-droppable")
        self.draggable = page.locator("#rect-draggable")
        self.text = page.locator("#text-droppable")


    @allure.step("Check two boxes are displayed")
    def should_have_default_state(self):
        expect(self.droppable).to_be_visible()
        expect(self.draggable).to_be_visible()


    @allure.step("Drag one box to another box")
    def drag_box_to_target(self):
        self.draggable.drag_to(self.droppable)


    @allure.step("Check text {text} in top box")
    def should_have_text_in_top_box(self, text):
        expect(self.text).to_have_text(text)


    @allure.step("Check the box is inside another box")
    def draggable_should_be_inside_droppable(self):
        expect(self.droppable.locator("#rect-draggable")).to_be_visible()


