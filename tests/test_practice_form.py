import pytest
import allure
from utils.allure_helper import attach_screenshot
from data.data_for_practice_form import (valid_required_data_to_fill, valid_first_all_data_to_fill,
                                         valid_third_all_data_to_fill, valid_second_all_data_to_fill,
                                         without, change_key)


@allure.feature("Practice Form")
@allure.story("Submitting Form")
@allure.title("Submitting form with only required fields filled")
def test_submit_form_with_only_required_fields_filled(practice_form_page):
    try:
        practice_form_page.open()
        practice_form_page.fill_input_fields_in_form(valid_required_data_to_fill)
        practice_form_page.submit_form()
        practice_form_page.should_have_result_popup_with_default_state(valid_required_data_to_fill)
        practice_form_page.close_modal_result()
    except Exception as e:
        attach_screenshot(practice_form_page.page, "error_screenshot")
        raise e


@pytest.mark.xfail(reason="Bug: City is not displayed")
@allure.feature("Practice Form")
@allure.story("Submitting Form")
@allure.title("Submitting form with all fields filled")
@pytest.mark.parametrize("all_data_to_fill", [valid_first_all_data_to_fill, valid_second_all_data_to_fill, valid_third_all_data_to_fill])
def test_submit_form_with_all_required_fields_filled(practice_form_page, all_data_to_fill):
    try:
        practice_form_page.open()
        practice_form_page.fill_input_fields_in_form(all_data_to_fill)
        practice_form_page.submit_form()
        practice_form_page.should_have_result_popup_with_default_state(all_data_to_fill)
        practice_form_page.close_modal_result()
    except Exception as e:
        attach_screenshot(practice_form_page.page, "error_screenshot")
        raise e



@allure.feature("Practice Form")
@allure.story("Submitting Form")
@allure.title("Trying submitting form without one required field filled")
@pytest.mark.parametrize("data_without_one_required_field", [without(valid_required_data_to_fill, "first_name"),
                                                             without(valid_required_data_to_fill, "last_name"),
                                                             without(valid_required_data_to_fill, "email"),
                                                             without(valid_required_data_to_fill, "gender"),
                                                             without(valid_required_data_to_fill, "mobile_number"),
                                                             without(valid_required_data_to_fill, "address_input")],
                         ids= ["data_without_first_name",
                               "data_without_last_name",
                               "data_without_email",
                               "data_without_gender",
                               "data_without_mobile_number",
                               "data_without_address_input"])
def test_try_submit_form_without_one_required_field_filled(practice_form_page, data_without_one_required_field):
    try:
        practice_form_page.open()
        practice_form_page.fill_input_fields_in_form(data_without_one_required_field)
        practice_form_page.submit_form()
        practice_form_page.should_not_submit()
    except Exception as e:
        attach_screenshot(practice_form_page.page, "error_screenshot")
        raise e



@allure.feature("Practice Form")
@allure.story("Submitting Form")
@allure.title("Trying submitting form with invalid phone number")
def test_try_submit_with_invalid_mobile_number(practice_form_page):
    try:
        practice_form_page.open()
        practice_form_page.fill_input_fields_in_form(
            change_key(valid_required_data_to_fill, "mobile_number", change="12-43-44"))
        practice_form_page.submit_form()
        practice_form_page.should_not_submit()
        practice_form_page.should_have_error_message("Mobile number must be exactly 10 digits")
    except Exception as e:
        attach_screenshot(practice_form_page.page, "error_screenshot")
        raise e


