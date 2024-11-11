# Topic 7: Web Automation with Playwright


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

1. Applicable for Web and API testing
2. Intuitive integration with Pytest Test Automation Framework
3. Intuitive integration with Allure
4. Inherited  support for all Python functionality
5. Easy to use within CI/CD (e.g. Jenkins)


## References:

1. [Playwright - Python official page](https://playwright.dev/python/)
2. [Installation](https://playwright.dev/python/docs/intro)
3. [Assertion](https://playwright.dev/python/docs/test-assertions)


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

# Framework structure
1 Service classes
2 Page object
3 Test suits

## Test suit top level components:

1. Import libraries
2. Import page Page Object(s)
3. Test
- Action
- Assertion



## Page object top level components:
1. Import libraries
2. PO constructor (including locators)
3. Methods of PO
- Interacting with page
- Getting information
- Assertion methods 


### PageObject

PageObject is the kernel of Playwright UI test

1. Import libraries
Page Object Structure exampe: 
```python
from playwright.sync_api import Page

2. PO constructor (including locators)
class PoClassNamePage:
    # Initialize page and selectors
    def __init__(self, page: Page):
        self.page = page
        # list of selectors
        self.fullNameField = page.locator("#userName")
        self.emailField = page.locator("#userEmail")
        self.currentAddressField = page.locator("#currentAddress")
        self.permanentAddressField = page.locator("#permanentAddress")
        self.submitButton = page.locator("#submit")
        self.pageLoadingIndicator = page.locator(".text-center")

3. Methods of PO
    # method to iteract with page
    def navigate(self, url: str):
        self.page.goto(url)
        self.currentAddressField .click()

    # method to get information
    def navigate(self, url: str):
        self.permanentAddressField.text_content()

    # Asserton methods
    def check_loading_page(self):
        return self.fullNameField.text_content() == "John Smith"
```
> [!TIP]
> locator can be organized like 'chain':

```python
self.access_block = page.locator("//*div[@id='add-visibility-form']")
self.access_block_select_type = self.access_block.locator("/div[@id='id_requied_action']") 
instead of "//*div[@id='add-visibility-form']/div[@id='id_requied_action']"
```

### Assertions
Playwright has specific assertion: expect(locator).assert_method()
Assert_method() are numerous:
expect(locator).to_be_hidden()	Element is not visible
expect(locator).to_be_in_viewport()	Element intersects viewport
expect(locator).to_be_visible()	Element is visible
expect(locator).to_contain_text()	Element contains text
expect(locator).to_have_accessible_description()	Element has a matching accessible description
expect(locator).to_have_accessible_name()	Element has a matching accessible name
expect(locator).to_have_attribute()	Element has a DOM attribute
..

> [!TIP]
> The main advantage of 'expect' - waiting for page loading with required parameter till framework's timer

#### 'expect' vs default Python 'assert'
'assert' returns Boolean
'expect' returns None

example:
```python
    def is_macros_not_displayed_on_page(self, macro_name: str) -> None:
        expect(self.page.locator(f"//*[text()[contains(.,'{macros_name}')]]")).not_to_be_visible()
```
compare with:
```python
    def is_macros_not_displayed_on_page(self, macro_name: str) -> bool:
        return self.page.locator(f"//*[text()[contains(.,'{macros_name}')]]").not_to_be_visible()
```
The last one can be used in test in way like:

```python
assert request_macros_page.is_macro_displayed_on_page(setup_ui_data["macro_name"])
```
It more convenient for code but sometimes not convenient in case of delay with page loading



### Additional features of Playwright vs Pytest

1. Playwright supports all standart types of locators like css or xpath. Additionally it provides the additional functionality like last and first locator:

```python
page.locator(".classname").last.click()
```
2. Ability operate with locator in "#shadow-root"
Remark: #shadow-root is area within DOM. Locators within this section are not available for many Test Automation Frameworks

3. Playwright has numerous build-in methods like:
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

### Action methods


    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)


    # Get information from page
    def check_loading_initial_page(self):
        return self.text_selenium.is_visible()



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
```

## Hometask

Create PO and test-suit for page https://demoqa.com/text-box with following scenario
- Add data like:
fullName = "Donald Duck";
email = "donald.duck@example.com";
currentAddress = "56 Main St";
permanentAddress = "379 Apple Rd";
- Click Submit button
- Check that data is displayed as expected
Name:Donald Duck
Email:donald.duck@example.com
Current Address :56 Main St
Permananet Address :379 Apple Rd
