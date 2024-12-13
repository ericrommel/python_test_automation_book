from playwright.sync_api import Page


class StartingPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.login_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.next_page_logo = page.locator(".app_logo")

    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)

    # Get information from page
    def fill_login_data(self, name: str, password: str) -> None:
        self.login_field.click()
        self.login_field.fill(name)
        self.password_field.click()
        self.password_field.fill(password)
        self.login_button.click()

    def check_login_is_correct(self) -> str:
        return self.next_page_logo.inner_text()
