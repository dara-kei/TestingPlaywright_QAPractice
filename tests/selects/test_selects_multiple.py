from data.travel_options import Places, Transport, Date
import pytest
import allure
from utils.allure_helper import attach_screenshot


@pytest.mark.positive
@allure.feature("Multiple selects")
@allure.title("Checking selects default state")
@allure.description("""
Requirements:
- There should be 3 fields:
- Choose the place you want to go
- Choose how you want to get there
- Choose when you want to go
- All the fields are required.
""")
def test_selects_multiple_page_initial_state(select_multiple_page) -> None:
    try:
        select_multiple_page.open()
        select_multiple_page.should_have_default_state()
    except Exception as e:
        attach_screenshot(select_multiple_page.page, "error_screenshot")
        raise e



# # в этом тесте будут перебираться все комбинации (60 тестов!), что избыточно, хотя в данном тесте меньше по коду
# @pytest.mark.parametrize("select1_value", [x.value for x in Places])
# @pytest.mark.parametrize("select2_value", [x.value for x in Transport])
# @pytest.mark.parametrize("select3_value", [x.value for x in Date])
# def test_submit_with_all_selects_selected(select_multiple_page, select1_value,select2_value,select3_value) -> None:
#     select_multiple_page.open()
#     select_multiple_page.choose_select_option(0, select1_value)
#     select_multiple_page.choose_select_option(1, select2_value)
#     select_multiple_page.choose_select_option(2, select3_value)
#     select_multiple_page.submit()
#     select_multiple_page.should_have_result_text(f"to go by {select2_value.lower()} to the {select1_value.lower()} {select3_value.lower()}")


@pytest.mark.positive
@allure.feature("Multiple selects")
@allure.title("Checking submission with all selects selected (all options of select Places")
@allure.description("""
Requirements:
- User should be able to select any option in each field
- The result can be sent using the Submit button
- After submitting the form, the option selected by the user should be placed into the resulting phrase and displayed to the user
- Resulting phrase template: "to go by <transport> to the <destination> <when>"
""")
@pytest.mark.parametrize("select1_value", [x.value for x in Places])
def test_submit_with_all_first_select_options(select_multiple_page, select1_value) -> None:
    try:
        select_multiple_page.open()
        select_multiple_page.choose_select_option(0, select1_value)
        select_multiple_page.choose_select_option(1, "Car")
        select_multiple_page.choose_select_option(2, "Today")
        select_multiple_page.submit()
        select_multiple_page.should_have_result_text(f"to go by car to the {select1_value.lower()} today")
    except Exception as e:
        attach_screenshot(select_multiple_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Multiple selects")
@allure.title("Checking submission with all selects selected (all options of select Transport")
@allure.description("""
Requirements:
- User should be able to select any option in each field
- The result can be sent using the Submit button
- After submitting the form, the option selected by the user should be placed into the resulting phrase and displayed to the user
- Resulting phrase template: "to go by <transport> to the <destination> <when>"
""")
@pytest.mark.parametrize("select2_value", [x.value for x in Transport])
def test_submit_with_all_second_select_options(select_multiple_page, select2_value) -> None:
    try:
        select_multiple_page.open()
        select_multiple_page.choose_select_option(0, "Mountains")
        select_multiple_page.choose_select_option(1, select2_value)
        select_multiple_page.choose_select_option(2, "Tomorrow")
        select_multiple_page.submit()
        select_multiple_page.should_have_result_text(f"to go by {select2_value.lower()} to the mountains tomorrow")
    except Exception as e:
        attach_screenshot(select_multiple_page.page, "error_screenshot")
        raise e


@pytest.mark.positive
@allure.feature("Multiple selects")
@allure.title("Checking submission with all selects selected (last option of select Data")
@allure.description("""
Requirements:
- User should be able to select any option in each field
- The result can be sent using the Submit button
- After submitting the form, the option selected by the user should be placed into the resulting phrase and displayed to the user
- Resulting phrase template: "to go by <transport> to the <destination> <when>"
""")
def test_submit_with_last_option_of_third_select(select_multiple_page) -> None:
    try:
        select_multiple_page.open()
        select_multiple_page.choose_select_option(0, "Old town")
        select_multiple_page.choose_select_option(1, "Train")
        select_multiple_page.choose_select_option(2, "Next week")
        select_multiple_page.submit()
        select_multiple_page.should_have_result_text(f"to go by train to the old town next week")
    except Exception as e:
        attach_screenshot(select_multiple_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
@allure.feature("Multiple selects")
@allure.title("Trying submitting with one select not selected ")
@allure.description("""
Requirements:
- All the fields are required.
""")
# Проверка, что все dropdown обязательные через не нажатие одного
@pytest.mark.parametrize(
    "select1_index, text1, select2_index, text2",[(1, "Car", 2, "Today"),
                                                  (0, "Sea", 2, "Today"),
                                                  (0, "Sea", 1, "Car")]
)
def test_not_submission_with_one_select_not_selected(select_multiple_page, select1_index, text1, select2_index, text2) -> None:
    try:
        select_multiple_page.open()
        select_multiple_page.choose_select_option(select1_index, text1)
        select_multiple_page.choose_select_option(select2_index, text2)
        select_multiple_page.submit()
        select_multiple_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(select_multiple_page.page, "error_screenshot")
        raise e


@pytest.mark.negative
def test_not_submission_when_no_option_selected(select_multiple_page):
    try:
        select_multiple_page.open()
        select_multiple_page.submit()
        select_multiple_page.should_not_have_result()
    except Exception as e:
        attach_screenshot(select_multiple_page.page, "error_screenshot")
        raise e