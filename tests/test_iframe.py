def test_iframe_with_sample_page(iframe_page):
    iframe_page.open()
    iframe_page.should_have_iframe()
    iframe_page.should_not_have_empty_iframe()

