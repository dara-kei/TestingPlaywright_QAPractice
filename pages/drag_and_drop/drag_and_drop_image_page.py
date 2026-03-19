from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class DragAndDropImagePage(BasePage):
    URL = "https://www.qa-practice.com/elements/dragndrop/images"
    def __init__(self, page : Page) -> None:
        super().__init__(page)
        self.droppable_boxes = { "top": page.locator("#rect-droppable1"), "bottom" : page.locator("#rect-droppable2")}
        self.img = page.locator("img[src='/static/home/smile.png']")


    @allure.step("Check the default state of boxes")
    def should_have_default_state(self):
        with allure.step("Check boxes count"):
            expect(self.page.locator(".rect-droppable")).to_have_count(2)
        with allure.step("Check boxes are displayed"):
            expect(self.droppable_boxes["bottom"]).to_be_visible()
            expect(self.droppable_boxes["top"]).to_be_visible()
        with allure.step("Check one img is displayed"):
            expect(self.droppable_boxes["bottom"].locator("img")).to_be_visible()
            expect(self.page.locator("#rect-droppable2 img")).to_have_count(1)


    @allure.step("Drag img to another box")
    def drag_image_to_box(self, droppable_box):
        self.img.drag_to(self.droppable_boxes[droppable_box])


    @allure.step("Check img is displayed in other box")
    def should_have_img_in_other_box(self, droppable_box, text):
        expect(self.droppable_boxes[droppable_box]).to_have_text(text)


    @allure.step("Check the img is inside another box")
    def should_have_image_inside_box(self, droppable_box):
        expect(self.droppable_boxes[droppable_box].locator("img")).to_be_visible()


    @allure.step("Check the previous box is empty")
    def should_have_empty_box(self, droppable_box):
        expect(self.droppable_boxes[droppable_box].locator("img")).not_to_be_visible()
