import allure
from utils.allure_helper import attach_screenshot


@allure.feature("New tab open with link")
@allure.title("Checking opening new tab with link")
@allure.description("""
Requirements:
- The button should open the page /elements/new_tab/new_page
- New page should be opened in a new tab
""")
def test_new_tab_link_should_open_new_page(new_tab_link_page) -> None:
    try:
        new_tab_link_page.open()
        new_tab_link_page.check_new_page()
        new_tab_link_page.should_keep_original_page_url()
    except Exception as e:
        attach_screenshot(new_tab_link_page.page, "error_screenshot")
        raise e

