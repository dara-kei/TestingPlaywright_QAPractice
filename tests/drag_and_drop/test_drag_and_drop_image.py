def test_drag_and_drop_image_page_initial_state(drag_and_drop_image_page):
    drag_and_drop_image_page.open()
    drag_and_drop_image_page.should_have_default_state() # должен падать, так как смайл не в том окне по требованиям

def test_drag_and_drop_image_between_boxes(drag_and_drop_image_page):
    drag_and_drop_image_page.open()
    for _ in range(3):
        drag_and_drop_image_page.drag_image_to_box("bottom")
        drag_and_drop_image_page.should_be_dropped_successfully("bottom")
        drag_and_drop_image_page.should_have_image_inside_box("bottom")
        drag_and_drop_image_page.should_have_empty_box("top")
        drag_and_drop_image_page.drag_image_to_box("top")
        drag_and_drop_image_page.should_be_dropped_successfully("top")
        drag_and_drop_image_page.should_have_image_inside_box("top")
        drag_and_drop_image_page.should_have_empty_box("bottom")


