def test_new_tab_link_should_open_new_page(new_tab_link_page) -> None:
    new_tab_link_page.open()
    new_tab_link_page.check_new_page()
    new_tab_link_page.should_keep_original_page_url()

