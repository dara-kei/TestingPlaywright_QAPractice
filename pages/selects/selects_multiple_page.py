from playwright.sync_api import Page, expect
from pages.selects.base_select_page import BaseSelectPage


class SelectsMultiplePage(BaseSelectPage):
    URL = "https://www.qa-practice.com/elements/select/mult_select"


    def __init__(self, page: Page):
        super().__init__(page)
        self.selects = [page.locator("#id_choose_the_place_you_want_to_go"),
                      page.locator("#id_choose_how_you_want_to_get_there"),
                      page.locator("#id_choose_when_you_want_to_go")]


    def choose_select_option(self, select_index: int, option: str) -> None:
        self.selects[select_index].select_option(option)


    def should_have_default_state(self) -> None:
        expect(self.page.locator('//select[@class="select form-select"]')).to_have_count(3)
        expect(self.page.locator(f'label[for="id_choose_the_place_you_want_to_go"]')).to_have_text(
            "Choose the place you want to go*")
        expect(self.page.locator(f'label[for="id_choose_how_you_want_to_get_there"]')).to_have_text(
            "Choose how you want to get there*")
        expect(self.page.locator(f'label[for="id_choose_when_you_want_to_go"]')).to_have_text("Choose when you want to go*")
        expect(self.selects[0]).to_have_attribute("required", "")
        expect(self.selects[1]).to_have_attribute("required", "")
        expect(self.selects[2]).to_have_attribute("required", "")





