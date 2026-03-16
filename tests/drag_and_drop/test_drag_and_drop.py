def test_drag_and_drop_page_initial_state(drag_and_drop_boxes_page):
    drag_and_drop_boxes_page.open()
    drag_and_drop_boxes_page.should_have_default_state()


def test_dragging_bottom_box_to_top_one(drag_and_drop_boxes_page):
    drag_and_drop_boxes_page.open()
    drag_and_drop_boxes_page.drag_box_to_target()
    drag_and_drop_boxes_page.should_be_dropped_successfully()
    drag_and_drop_boxes_page.draggable_should_be_inside_droppable()

