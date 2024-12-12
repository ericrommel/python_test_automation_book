import pytest
from selenium.webdriver.common.by import By
from ..core.browser import Browser
from ..core.logger import Logger
from ..business.login_actions import LoginActions
from ..data.config import Config


@pytest.fixture
def setup_browser():
    driver = Browser.get_browser()
    yield driver
    driver.quit()


@pytest.fixture
def test_data():
    return Config.get_test_data()


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),  # Valid login
        ("invaliduser", "SuperSecretPassword!", "Your username is invalid!"),  # Invalid username
        ("tomsmith", "wrongpassword", "Your password is invalid!"),  # Invalid password
    ],
)
def test_login_scenarios(setup_browser, test_data, username, password, expected_message):
    logger = Logger.get_logger("TestLoginScenarios")
    logger.info("Starting login test")

    driver = setup_browser
    driver.get(f"{Config.BASE_URL}/login")

    login_actions = LoginActions(driver)
    login_actions.enter_username(username)
    login_actions.enter_password(password)
    login_actions.click_login()

    alert_message = driver.find_element(By.CSS_SELECTOR, "div.flash").text
    assert expected_message in alert_message
    logger.info(f"Test for {username} passed.")


def test_browser_failure():
    with pytest.raises(ValueError, match="Unsupported browser: firefox"):
        Browser.get_browser("firefox")


@pytest.mark.skip(reason="Test case under construction")
def test_feature_in_progress():
    pytest.skip("Skipping test for unimplemented feature")
