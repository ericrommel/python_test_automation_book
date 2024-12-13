import time

import pytest
from login_page_object import StartingPage
from playwright.sync_api import sync_playwright

# user_name = "standard_user"
# user_password = "secret_sauce"

# Define a pytest fixture to set up Playwright and browser instance
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    return page


# Test case using the StartingPage object
def test_login(page, setup_data):
    login_page = StartingPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.fill_login_data(setup_data["user_name"], setup_data["user_password"])
    time.sleep(1)
    assert login_page.check_login_is_correct() == "Swag Labs"
