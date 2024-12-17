import time

from login_page_object import StartingPage
from playwright.sync_api import sync_playwright

user_name = "standard_user"
user_password = "secret_sauce"


# Define a pytest fixture to set up Playwright and browser instance
def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login_page = StartingPage(page)
        login_page.navigate("https://www.saucedemo.com/")
        login_page.fill_login_data(user_name, user_password)
        time.sleep(1)
        assert login_page.check_login_is_correct() == "Swag Labs"
        browser.close()


if __name__ == "__main__":
    main()