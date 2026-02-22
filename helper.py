def submit(page: Page, url: str, loc: str, text: str) -> None:
    """
    Helper function
    Used in:
    test_input_email.py,
    test_input_password.py,
    test_input_text.py

    """
    page.goto(url)
    page.locator(loc).click()
    page.locator(loc).fill(text)
    page.locator(loc).press("Enter")

