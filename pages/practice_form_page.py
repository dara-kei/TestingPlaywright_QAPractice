from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    URL = "https://www.qa-practice.com/forms/practice-form"

    def __init__(self, page:Page):
        super().__init__(page)
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#userEmail")
        self.gender_checkboxes = {"male" : page.locator("#gender_0"),
                                  "female" : page.locator("#gender_1"),
                                  "other" : page.locator("#gender_2")}
        self.mobile_number_input = page.locator("#userNumber")
        self.subjects_input = page.locator("#subjectsAutocomplete") # "Social Studies", "Sanskrit"
        self.hobbies_checkboxes = {"sports" : page.locator("#hobbies_0"),
                        "reading" : page.locator("#hobbies_1"),
                        "music" : page.locator("#hobbies_2")}
        self.picture_upload = page.locator("#uploadPicture")
        self.current_address = page.locator("#currentAddress")
        self.state_select = page.locator("#state")
        self.city_select = page.locator("#city")
        self.submit_button = page.locator("#submit-id-submit")

        # modal results
        self.result_modal = page.locator("#resultsModal")
        self.result_modal_title = page.locator(".modal-title")
        self.modal_close_button = page.locator("#closeSmallModal-userForm")
        self.student_name = page.locator("#resultsTable tr:nth-child(1) td:nth-child(2)")
        self.student_email = page.locator("#resultsTable tr:nth-child(2) td:nth-child(2)")
        self.gender = page.locator("#resultsTable tr:nth-child(3) td:nth-child(2)")
        self.mobile = page.locator("#resultsTable tr:nth-child(4) td:nth-child(2)")
        self.subjects = page.locator("#resultsTable tr:nth-child(5) td:nth-child(2)")
        self.hobbies = page.locator("#resultsTable tr:nth-child(6) td:nth-child(2)")
        self.picture = page.locator("#resultsTable tr:nth-child(7) td:nth-child(2)")
        self.address = page.locator("#resultsTable tr:nth-child(8) td:nth-child(2)")
        self.state_and_city = page.locator("#resultsTable tr:nth-child(9) td:nth-child(2)")




    def submit_form(self):
        self.submit_button.click()


    def fill_input_fields_in_form(self, data_to_fill: dict):
        if "first_name" in data_to_fill:
            self.first_name_input.fill(data_to_fill["first_name"])
        if "last_name" in data_to_fill:
            self.last_name_input.fill(data_to_fill["last_name"])
        if "email" in data_to_fill:
            self.email_input.fill(data_to_fill["email"])
        if "mobile_number" in data_to_fill:
            self.mobile_number_input.fill(data_to_fill["mobile_number"])
        if "subjects_input" in data_to_fill:
            self.subjects_input.fill(data_to_fill["subjects_input"])
        if "address_input" in data_to_fill:
            self.current_address.fill(data_to_fill["address_input"])


    def select_checkbox(self,
                        gender_checkbox = None,
                        hobby_checkbox = None):
        if gender_checkbox is not None:
            self.gender_checkboxes[gender_checkbox].check()
        if hobby_checkbox is not None:
            self.hobbies[hobby_checkbox].check()


    def should_have_result_popup_with_default_state(self, data_to_fill):
        expect(self.result_modal_title).to_have_text("Thanks for submitting the form")
        expect(self.student_name).to_have_text(data_to_fill["first_name"] + " " + data_to_fill["last_name"])
        expect(self.student_email).to_have_text(data_to_fill["email"])
        expect(self.gender).to_have_text(data_to_fill["gender"])
        expect(self.mobile).to_have_text(data_to_fill["mobile_number"])
        expect(self.subjects).to_have_text(data_to_fill["subjects"])
        expect(self.hobbies).to_have_text(data_to_fill["hobbies"])
        expect(self.picture).to_have_text(data_to_fill["picture"])
        expect(self.address).to_have_text(data_to_fill["address_input"])
        expect(self.state_and_city).to_have_text(data_to_fill["current_address"])

    def close_result_popup(self):
        self.modal_close_button.click()








