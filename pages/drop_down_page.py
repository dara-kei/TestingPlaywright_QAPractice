from playwright.sync_api import Page, expect
import enum

URL = "https://www.qa-practice.com/elements/select/single_select"

class DropDownPage:
    def __init__(self, page: Page):
        self.page = page
        self.select_locator = page.locator("#id_choose_language")
        self.submit_btn_locator = page.locator("#submit-id-submit")
        self.result_text_locator = page.locator("#result-text")
        self.field_name = page.locator("label[for='id_choose_language']")

    def submit(self):
        self.submit_btn_locator.click()

    def select_language(self, language: str) -> None:
        self.select_locator.select_option(language)

    def result_should_have_text(self, expected_result) -> None:
        expect(self.result_text_locator).to_have_text(expected_result)
        # разобраться с soft для того, если много expect в def то, если 1 expect упадет, то он продолжит проверку expect-ов в этом тесте

    def result_should_not_exist(self):
        expect(self.result_text_locator).to_have_count(0)

    def field_should_be_required(self):
        expect(self.select_locator).to_have_attribute("required", "")

    def should_have_field_name(self) -> None:
        expect(self.field_name).to_have_text("Choose language*")

    def open_url(self):
        self.page.goto(URL)




class ProgrammingLanguage(enum.Enum):

    # с помощью enum создаем перечисление ProgrammingLanguage, в котором:
    # PYTHON — это имя элемента
    # "Python" — его значение

    # ProgrammingLanguage.PYTHON - это объект enum, у которого:
    # ProgrammingLanguage.PYTHON.name   # "PYTHON"
    # ProgrammingLanguage.PYTHON.value  # "Python"


    PYTHON = "Python"
    JAVASCRIPT = "JavaScript"
    JAVA = "Java"
    RUBY = "Ruby"
    SHARP = "C#"