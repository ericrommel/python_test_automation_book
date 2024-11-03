# Week 7: Web Automation with Playwright


## Summary:

Playwright is the powerful tool for Web Test automation (UI and API) in different programming languages:
- TypeScript, 
- JavaScript,
- .NET,
- Java.
- Python

Playwright is 
- Cross-browser,
- Cross-platform,
- Support mobile testing

The scope of this page: Playwright - Python


## Playwright - Python General information:

1. Convenient for Web and API testing
2. Intuitive integration with Pytest Test Automation Framework
3. Intuitive integration with Allure
4. Inherited  support for all Python functionality
5. Easy to use within CI/CD (e.g. Jenkins)


## References:

1. [Playwright - Python oficial page](https://playwright.dev/python/)
2. [Installation](https://playwright.dev/python/docs/intro)
3. 


## Installation:

From Python point of view Playwright is just a package

Installation: 
```python
pip install pytest-playwright
```


## Launching:

The simplest launching command: 
```python
pytest filename_with_playwright_code.py
```


## Test:

1. Action
2. Assertion
3. TBD


## UI testing components


### PageObject

PageObject is the kernel of Playwright UI test

To use it need to import related library: 
```python
from playwright.sync_api import Page
```

### Locators

Playwright supports all standart types of locators like css or xpath. Additionally it provides the additional functionality like below:
1. Last and first locator:

```python
page.locator(.classname).last.click()
```

3. Ability operate with locator in "#shadow-root"
Remark: #shadow-root is area within DOM. Locators within this section are not available for many Test Automation Frameworks
4. The numerous build-in methods like:
   
3.1
   .to_have_text()

```python
page.get_by_role("#Category")).to_have_text(["plates", "caps", "catleriese"])
```

3.2
   .get_by_text()
```python
page.get_by_text("orange").click()
```

from playwright.sync_api import Page

class StartingPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.text_selenium = page.locator("[alt='Selenium Online Training']")


    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)


    # Get information from page
    def check_loading_initial_page(self):
        return self.text_selenium.is_visible()

The important part of playwright is 'expect'

'assert' returns Boolean

'expect' returns None

The main advantage of 'expect' - waiting for page loading with required parameter till framework's timer

### Example of code

#### Page object
staring_page.py
```python
from playwright.sync_api import Page

class StartingPage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        self.text_selenium = page.locator("[alt='Selenium Online Training']")


    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)


    # Get information from page
    def check_loading_initial_page(self):
        return self.text_selenium.is_visible()
```
#### Test suit

test_starting_page.py
```python
import pytest
from starting_page import StartingPage
from playwright.sync_api import sync_playwright

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
def test_login(page):
    login_page = StartingPage(page)
    login_page.navigate("https://demoqa.com")

    # Assertion example - page check
    assert login_page.check_loading_initial_page()
```

#### Launching
1. Save PO and test suit in same folder
2. Run command: pytest '\test_starting_page.py
