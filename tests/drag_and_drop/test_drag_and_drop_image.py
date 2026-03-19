import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.xfail(reason="Bug: img is in wrong square", strict=False)
@allure.feature("Drag and drop image")
@allure.title("Checking drag and drop image page")
@allure.description("""
Requirements:
- There should be two squares on the page
- There should be a smiley in the bottom square
""")
def test_drag_and_drop_image_page_initial_state(drag_and_drop_image_page):
    try:
        drag_and_drop_image_page.open()
        drag_and_drop_image_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(drag_and_drop_image_page.page, "error_screenshot")
        raise e


@allure.feature("Drag and drop image")
@allure.title("Checking dragging image from box to box")
@allure.description("""
Requirements:
- The smiley can be dragged from square to square an infinite number of times
- When dropping the smiley into any of the squares, the text is "Dropped!" should appear in this square
- A square without a smiley must be completely empty
""")
def test_drag_and_drop_image_between_boxes(drag_and_drop_image_page):
    drag_and_drop_image_page.open()
    for _ in range(3):
        try:
            drag_and_drop_image_page.drag_image_to_box("bottom")
            drag_and_drop_image_page.should_have_img_in_other_box("bottom", "Dropped!")
            drag_and_drop_image_page.should_have_image_inside_box("bottom")
            drag_and_drop_image_page.should_have_empty_box("top")
            drag_and_drop_image_page.drag_image_to_box("top")
            drag_and_drop_image_page.should_have_img_in_other_box("top", "Dropped!")
            drag_and_drop_image_page.should_have_image_inside_box("top")
            drag_and_drop_image_page.should_have_empty_box("bottom")
        except Exception as e:
            attach_screenshot(drag_and_drop_image_page.page, "error_screenshot")
            raise e


