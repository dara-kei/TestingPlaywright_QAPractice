from playwright.sync_api import Page, expect
import re

def test_area_single_initial_state(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.should_have_default_state()


def test_submit_when_text_area_filled(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.fill("Hello!")
    text_area_single_page.submit()
    text_area_single_page.should_have_result_text("Hello!")


def test_submit_when_text_area_not_filled(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.submit()
    text_area_single_page.should_not_have_result()



def test_submit_when_text_area_filled_with_only_spaces(text_area_single_page) -> None:
    text_area_single_page.open()
    text_area_single_page.fill("  ")
    text_area_single_page.submit()
    text_area_single_page.should_have_error_message("This field is required.")




