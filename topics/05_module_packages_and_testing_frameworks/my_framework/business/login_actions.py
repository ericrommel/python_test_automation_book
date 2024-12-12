from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.clear()
            username_field.send_keys(username)
        except Exception as e:
            raise Exception(f"Error entering username: {e}")

    def enter_password(self, password):
        try:
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_field.clear()
            password_field.send_keys(password)
        except Exception as e:
            raise Exception(f"Error entering password: {e}")

    def click_login(self):
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            login_button.click()
        except Exception as e:
            raise Exception(f"Error clicking login button: {e}")
