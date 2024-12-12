# Python Test Automation Framework with Selenium

This is just a sample to demonstrate a simple `Test Automation Framework (TAF)` using `Python`, `Selenium WebDriver`, and `Pytest`.

The example focuses on a login functionality test, showcasing both positive and negative test scenarios. The framework employs `modular design` principles to organize the layers:

1. Business logic
2. Core utilities
3. Data
4. Tests


## TAF Structure

```plain-text
root/
-- topics/
----- 05_module_packages_and_testing_frameworks/
-------- my_framework/
----------- business/
-------------- login_actions.py
----------- core/
-------------- browser.py
-------------- logger.py
----------- data/
-------------- config.py
-------------- test_data.json
----------- tests/
-------------- test_login.py
```

1. `business/`: Contains actions related to specific business processes.
   - `login_actions.py`: Encapsulates login-related actions.
2. `core/`: Core utilities required by the framework.
   - `browser.py`: Handles browser setup using `Selenium WebDriver` and `webdriver-manager`.
   - `logger.py`: Configures logging.
3. `data/`: Stores test data and configurations.
   - `config.py`: Centralizes configuration and data retrieval.
   - `test_data.json`: `JSON` file containing test inputs.
4. `tests/`: Houses test scripts written with `pytest`.
   - test_login.py: Implements login tests.


## Setup and Prerequisites

1. Install Required Tools: Ensure the following are installed on your system: `Python` and `pip` (Python package manager)
2. Install Required Python Libraries:

   ```bash
   $ pip install selenium webdriver-manager pytest
   ```


## Execution Instructions


### Step 1: Understand the Test Scenarios

The framework includes the following test scenarios:
- **Positive Case:**
  - Valid login using correct username and password.
- **Negative Cases:**
  - Invalid username with valid password.
  - Valid username with invalid password.


### Step 2: Run the Tests

Navigate to the tests directory and execute the tests using `Pytest`. Run the following command:

```bash
$ pytest test_login.py -v
```


### Step 3: View Results

Test results will be displayed in the console. Logs will be saved to `test_log.log` in the root directory.


## Practice Tasks (Drill)

1. Expand the framework to include additional test scenarios.
2. Save the logs inside the TAF structure
3. Integrate reporting tools like `pytest-html` for better visualization.
4. Note that the test execution is too slowly. The issue is, we are creating a new browser instance for each test case. Each `DevTools connection` happens when a new browser session is initiated, which is time-consuming. Your task here is optimized your TAF to reuse the same browser instance for all test cases that don't require isolated sessions.
> [!TIP]
> Use a `class-based` test structure with `session-level` fixtures to creating the browser instance once per test class or test session.
> Clean up after each test case (e.g., resetting state or navigating back to a starting page).
> Use parallel test execution with `pytest-xdist`, which can further reduce overall runtime.
