import allure
from utils.allure_helper import attach_screenshot
import pytest


@pytest.mark.positive
@allure.feature("Drag and drop boxes")
@allure.title("Checking drag and drop boxes page")
@allure.description("""
Requirements:
- There should be two squares on the page
""")
def test_drag_and_drop_page_initial_state(drag_and_drop_boxes_page):
    try:
        drag_and_drop_boxes_page.open()
        drag_and_drop_boxes_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(drag_and_drop_boxes_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Drag and drop boxes")
@allure.title("Checking dragging one box to another")
@allure.description("""
Requirements:
- The bottom square must be draggable.
- When dragging the bottom square to the top one, the text "Dropped!" should appear in the top square.
- The bottom square can only be dragged once.
""")
def test_dragging_bottom_box_to_top_one(drag_and_drop_boxes_page):
    try:
       drag_and_drop_boxes_page.open()
       drag_and_drop_boxes_page.drag_box_to_target()
       drag_and_drop_boxes_page.should_have_text_in_top_box("Dropped!")
       drag_and_drop_boxes_page.draggable_should_be_inside_droppable()
    except Exception as e:
        attach_screenshot(drag_and_drop_boxes_page.page, "error_screenshot")
        raise e

