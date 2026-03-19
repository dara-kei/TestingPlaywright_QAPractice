from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import allure


class IframePage(BasePage):
    URL = "https://www.qa-practice.com/elements/iframe/iframe_page"
    def __init__(self, page: Page):
        super().__init__(page)
        self.iframe = page.locator("iframe")

    @allure.step("Check iframe is displayed on the page")
    def should_have_iframe(self):
        expect(self.iframe).to_have_count(1)


    @allure.step("Open iframe")
    def open_iframe(self):
        return self.page.frame_locator("iframe")


    @allure.step("Check iframe is not empty")
    def should_not_have_empty_iframe(self):
        new_page = self.open_iframe()
        expect(new_page.locator("h1")).to_have_text("Album example")
        # проверяем, что страница с контентом, а не с ошибкой 404


