import allure
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class BaseTabPage(BasePage):
    NEW_URL = None


    def __init__(self, page: Page, new_tab_locator: str):
        super().__init__(page)
        self.new_tab = page.locator(new_tab_locator)


    @allure.step("Open new tab")
    def open_new_page(self):
        # Ожидаем появление новой вкладки при клике
        with self.page.context.expect_page() as new_page_info:
            self.new_tab.click()
        new_page = new_page_info.value #  Получаем объект новой вкладки
        new_page.wait_for_load_state() #  Ждём полной загрузки новой страницы
        return new_page


    @allure.step("Check original page url is kept")
    def should_keep_original_page_url(self) -> None:
        expect(self.page).to_have_url(self.URL)     # Проверяем, что исходная вкладка осталась прежней


    @allure.step("Check new page data")
    def check_new_page(self) -> None:
        new_page = self.open_new_page()
        with allure.step("Check new page url"):
            expect(new_page).to_have_url(self.NEW_URL)
        with allure.step("Check result text is 'I am a new page in a new tab'"):
            expect(new_page.locator("#result-text")).to_have_text("I am a new page in a new tab")
