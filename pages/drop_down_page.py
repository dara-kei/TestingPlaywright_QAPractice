from playwright.sync_api import Page, expect
import enum

URL = "https://www.qa-practice.com/elements/select/single_select"

class DropDownPage():
    def __init__(self, page: Page):
        self.page = page
        self.select_locator = page.locator("#id_choose_language")
        self.submit_btn_locator = page.locator("#submit-id-submit")
        self.result_text_locator = page.locator("#result-text")

    def submit(self):
        self.submit_btn_locator.click()

    def select_language(self, language: str) -> None:
        self.select_locator.select_option(language)

    def check_result(self, expected_result) -> None:
        expect(self.result_text_locator).to_have_text(expected_result)
        # разобраться с soft для того, если много expect в def то, если 1 expect упадет, то он продолжит проверку expect-ов в этом тесте

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