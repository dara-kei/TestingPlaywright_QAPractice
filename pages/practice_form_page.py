from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pathlib import Path
import allure


class PracticeFormPage(BasePage):
    URL = "https://www.qa-practice.com/forms/practice-form"

    def __init__(self, page:Page):
        super().__init__(page)
        # ui elements locators
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.locator("#lastName")
        self.email_input = page.locator("#userEmail")
        self.gender_checkboxes = {"Male" : page.locator("#gender_0"),
                                  "Female" : page.locator("#gender_1"),
                                  "Other" : page.locator("#gender_2")}
        self.mobile_number_input = page.locator("#userNumber")
        self.subjects_input = page.locator("#subjectsAutocomplete")
        self.hobbies_checkboxes = {"Sports" : page.locator("#hobbies_0"),
                        "Reading" : page.locator("#hobbies_1"),
                        "Music" : page.locator("#hobbies_2")}
        self.picture_upload = page.locator("#uploadPicture")
        self.current_address = page.locator("#currentAddress")
        self.state_select = page.locator("#div_id_state .custom-dropdown-control")
        self.city_select = page.locator("#div_id_city .custom-dropdown-control")
        self.submit_button = page.locator("#submit-id-submit")

        # modal locators
        self.result_modal = page.locator("#resultsModal")
        self.result_modal_title = page.locator(".modal-title")
        self.modal_close_button = page.locator("#closeSmallModal-userForm")

        # modal results locators
        self.student_name = page.locator("#resultsTable tr:nth-child(1) td:nth-child(2)")
        self.student_email = page.locator("#resultsTable tr:nth-child(2) td:nth-child(2)")
        self.gender = page.locator("#resultsTable tr:nth-child(3) td:nth-child(2)")
        self.mobile = page.locator("#resultsTable tr:nth-child(4) td:nth-child(2)")
        self.subjects = page.locator("#resultsTable tr:nth-child(6) td:nth-child(2)")
        self.hobbies = page.locator("#resultsTable tr:nth-child(7) td:nth-child(2)")
        self.picture = page.locator("#resultsTable tr:nth-child(8) td:nth-child(2)")
        self.address = page.locator("#resultsTable tr:nth-child(9) td:nth-child(2)")
        self.state_and_city = page.locator("#resultsTable tr:nth-child(10) td:nth-child(2)")

        # errors locator
        self.error = page.locator("#error_1_id_mobile")


    # click buttons
    @allure.step("Submit the form")
    def submit_form(self):
        self.submit_button.click()


    @allure.step("Close result modal")
    def close_modal_result(self):
        self.modal_close_button.click()


    # fill data
    @allure.step("Upload the picture")
    def upload_picture(self, file_path: str):
        self.picture_upload.set_input_files(file_path)


    @allure.step("Fill the form with the date: {data_to_fill}")
    def fill_input_fields_in_form(self, data_to_fill: dict):
        if "first_name" in data_to_fill:
            self.first_name_input.fill(data_to_fill["first_name"])
        if "last_name" in data_to_fill:
            self.last_name_input.fill(data_to_fill["last_name"])
        if "email" in data_to_fill:
            self.email_input.fill(data_to_fill["email"])
        if "gender" in data_to_fill:
            self.gender_checkboxes[data_to_fill["gender"]].check()
        if "mobile_number" in data_to_fill:
            self.mobile_number_input.fill(data_to_fill["mobile_number"])
        if "subjects" in data_to_fill:
            for item in data_to_fill["subjects"]:
                self.subjects_input.fill(item)
                self.subjects_input.press("Enter")
        if "hobbies" in data_to_fill:
            for item in data_to_fill["hobbies"]:
                self.hobbies_checkboxes[item].check()
        if "picture" in data_to_fill:
            self.upload_picture(data_to_fill["picture"])
        if "address_input" in data_to_fill:
            self.current_address.fill(data_to_fill["address_input"])
        if "state" in data_to_fill:
            self.state_select.click()
            self.page.locator(f"div.custom-dropdown-option[data-value='{data_to_fill["state"]}']").click()
        if "city" in data_to_fill:
            self.city_select.click()
            self.page.locator(f"div.custom-dropdown-option[data-value='{data_to_fill["city"]}']").click()


    # processing the result
    @allure.step("Check the modal as a result of successful submitting the form")
    def should_have_result_popup_with_default_state(self, data_to_fill):
        with allure.step("Check the modal is displayed"):
            expect(self.result_modal).to_be_visible()
        with allure.step("Check the modal title is 'Thanks for submitting the form'"):
            expect(self.result_modal_title).to_have_text("Thanks for submitting the form")
        with allure.step("Check the entered data is displayed correctly in the fields"):
            expect(self.student_name).to_have_text(data_to_fill["first_name"] + " " + data_to_fill["last_name"])
            expect(self.student_email).to_have_text(data_to_fill["email"])
            expect(self.gender).to_have_text(data_to_fill["gender"])
            expect(self.mobile).to_have_text(data_to_fill["mobile_number"])
            if "subjects" in data_to_fill:
                result = ", ".join(data_to_fill["subjects"])
                expect(self.subjects).to_have_text(result)
            else:
                expect(self.subjects).to_have_text("Not provided")
            if "hobbies" in data_to_fill:
                result = ", ".join(data_to_fill["hobbies"])
                expect(self.hobbies).to_have_text(result)
            else:
                expect(self.hobbies).to_have_text("Not provided")
            if "picture" in data_to_fill:
                expect(self.picture).to_have_text(Path(data_to_fill["picture"]).name)
            else:
                expect(self.picture).to_have_text("Not provided")
            expect(self.address).to_have_text(data_to_fill["address_input"])
            if "state" in data_to_fill and "city" in data_to_fill:
                expect(self.state_and_city).to_have_text(data_to_fill["state"] + ", " + data_to_fill["city"] )


    # processing the result with errors
    @allure.step("Check the form should not be submitted")
    def should_not_submit_form(self):
        expect(self.result_modal).not_to_be_visible()

    @allure.step("Check error message is displayed")
    def should_have_error_message(self, error_message):
        expect(self.error).to_have_text(error_message)















