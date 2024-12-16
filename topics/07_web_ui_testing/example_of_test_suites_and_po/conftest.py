import time

import pytest
from login_page_object import StartingPage
import os

from playwright.sync_api import sync_playwright

@pytest.fixture
def setup_data():
    user_name = "standard_user"
    user_password = os.environ.get("DEMO241211")
    # user_password = "secret_sauce"
    return locals()

# Define a pytest fixture to set up Playwright and browser instance
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # browser = playwright.firefox.launch()
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    return page


@pytest.fixture
def login_to_page(page, setup_data):
    login_page = StartingPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.fill_login_data(setup_data["user_name"], setup_data["user_password"])