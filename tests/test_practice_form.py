import pytest
from data.data_for_practice_form import required_data_to_fill, first_all_data_to_fill



def test_submit_form_with_only_required_fields_filled(practice_form_page):
    practice_form_page.open()
    practice_form_page.fill_input_fields_in_form(required_data_to_fill)
    practice_form_page.submit_form()
    practice_form_page.should_have_result_popup_with_default_state(required_data_to_fill)
    practice_form_page.close_result_popup()


@pytest.mark.parametrize("all_data_to_fill", [first_all_data_to_fill])
def test_submit_form_with_all_required_fields_filled(practice_form_page, all_data_to_fill):
    practice_form_page.open()
    practice_form_page.fill_input_fields_in_form(all_data_to_fill)
    practice_form_page.submit_form()
    practice_form_page.should_have_result_popup_with_default_state(all_data_to_fill)
    practice_form_page.close_result_popup()

