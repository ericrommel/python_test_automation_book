# Topic 7: Web Automation with Playwright

## Basic approach of Web Automation
- DOM, 
- DevTool,
- Locators
- Selenium

### DOM
DOM (Document Object Model) 
The document currently loaded in each one of your browser tabs is represented by a document object model. This is a "tree structure" representation created by the browser that enables the HTML structure to be easily accessed by programming languages.

#### Links to read about DOM
- [What is DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [DOM Manipulating_documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [DOM introduction](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

### DevTool
DevTools (short for Developer Tools) are built-in utilities in web browsers that allow developers to inspect, debug, and optimize their web applications directly from the browser. They provide a range of powerful features that facilitate front-end development, testing, and performance analysis, making it easier to understand how web pages are constructed and behave.
It is a part of many browsers particularly in Chrome, Firefox, Safari, and Edge

It incorporates several panels
For Web Automation the most important is Elements Panel:
It contains DOM
It allows viewing and edit the HTML structure and CSS styles of a webpage in real-time. You can change attributes, add styles, and see how these affect the page immediately.
Layout and Box Model: Visualize elements’ layout properties like padding, margin, border, and dimensions.

### Locators
Locators are used to identify and interact with WebElements within a web page’s Document Object Model (DOM). They serve as the foundation for automating web application tests by allowing testers to perform actions such as clicking buttons, entering text, or verifying content.
In Python locators are objects that are created by using /consuming string that define the place of element within DOM

The syntax of creating locator depends on of used library and the Test Framework. Below are examples for Selenium and Python Playwright

#### The most typical types of Locators
##### ID Locator: 
Targets elements with a unique id attribute. It's the fastest and most reliable locator if available.

Examples for DOM:

```xml
<div>
    <h1>Header 1</h1>
    <ul> Menu 1
        <li>Item 1</li>
        <li class='item2'>Item 2</li>
        <li id='item3'>Item 3</li>
        <li name='item4'>Item 4</li>
        <li input>Item 4</li>
        <li>Item5</li>
    </ul>
    <input type="hidden" name="type" class="js-site-search-type-field">
    <div class="example-class">
        <a>Click Here</a>
</div>
```

In Selenium:
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
element = driver.find_element("id", "item3")
element.click()
driver.quit()
```

In Playwright:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    element = page.locator("#item3")
    element.click()
    browser.close()
```

##### Class Name Locator: 
Matches elements by their class attribute, often used for elements styled similarly.
In Selenium:
```python
element = driver.find_element("class name", "item2")
element.click()
```
In Playwright:
```python
element = page.locator(".item2")
element.click()
```
##### Name Locator: 
Uses the name attribute of elements, commonly used for form inputs.
In Selenium:
```python
element = driver.find_element("name", "item4")
```
In Playwright:
```python
element = page.locator("[name='item4']")
```

##### Tag Name Locator:
Locates elements based on their HTML tag (e.g., input, div).
In Selenium:
```python
element = driver.find_element("tag name", "input")
```
In Playwright:
```python
element = page.locator("input")
```

##### Link Text Locator:
Identifies hyperlinks by their full text within <a> tags.

Examples
In Selenium:
```python
element = driver.find_element("link text", "Click Here") 
```
In Playwright:
```python
element = page.locator("text='Click Here'")
```

##### Partial Link Text Locator: 
Matches hyperlinks with a substring of their text.

Examples
In Selenium:
```python
element = driver.find_element("partial link text", "Click") 
```
In Playwright:
```python
element = page.locator("text='Click'")
```


##### CSS Selector: 
Allows selection of elements using CSS rules, offering advanced querying capabilities.

Examples
In Selenium:
```python
element = driver.find_element("css selector", "div.example-class > a") 
```
In Playwright:
```python
element = page.locator("div.example-class > a") 
```


##### XPath Locator: 
Uses XPath expressions to navigate the DOM, highly useful for complex structures or when no unique attributes exist.

Examples
In Selenium:
```python
element = driver.find_element("xpath", "//*div[@class='example-class']/a[text()='Click Here']")
```
In Playwright:
```python
element = page.locator("//*div[@class='example-class']/a[text()='Click Here']")
```
#### Locator Parent, sibling, child
- Parent: locator at level above the current locator
- Child: locator at level below the current locator
- Sibling: locator at same level of the current locator

Parent, sibling, child are used e.g. when target locator is difficult to identify (e.g. no id, name or complex class) while parent or child is easy to identify (e.g. it has id)

#### Links to read about Locators
- [Locators1](https://toolsqa.com/selenium-webdriver/selenium-locators)
- [Locators2](https://www.browserstack.com/guide/locators-in-seleniu)
- [Locators3 from Selenium](https://www.selenium.dev/documentation/webdriver/elements/locators)

### Selenium WebDriver
Selenium WebDriver is a widely used web automation tool that allows developers and testers to automate browser interactions for testing web applications. It is part of the Selenium suite and provides a programming interface to interact directly with web browsers like Chrome, Firefox, Edge, and Safari. Here's an overview:

#### Key Features of Selenium WebDriver:

| Feature       | Desctiption      |
|-----------------|----------------|
| Browser Automation | Simulates user actions such as clicking, typing, scrolling, and navigation. |
| Cross-Browser Testing | Supports multiple browsers for testing (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox)|
| Programming Language Support| Compatible with popular programming languages, including Python, Java, C#, Ruby, and JavaScript.|
| Direct Browser Control| Communicates directly with the browser, leading to faster and more reliable test execution.|

#### Use Cases:
- Automated functional testing.
- Regression testing of web applications.
- End-to-end testing for multi-page workflows.
- Performance and compatibility testing across browsers.

How does it Works (code example - Python):

```python
from selenium import webdriver

# Set up WebDriver
driver = webdriver.Chrome()  # Replace with Firefox, Edge, etc., as needed

# Open a website
driver.get("https://example.com")

# Find an element and interact
element = driver.find_element("id", "example-id")
element.click()

# Close the browser
driver.quit()
```

#### Official site: 
[Selenium](https://www.selenium.dev)


## Playwright Summary:

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

## Playwright - Python General information:

1. Applicable for Web and API testing
2. Intuitive integration with Pytest Test Automation Framework
3. Intuitive integration with Allure
4. Inherited  support for all Python functionality
5. Easy to use within CI/CD (e.g. Jenkins)

## Remark
Playwright is one of numerous test frameworks that use/support Python
Some other popular Python Test Frameworks:
1. Robot Test Framework: powerful frameworks that can be used without deep knowledge of Python. It allows creating tests that are convenient for reading by non-technical stakeholders. Website: robotframework.org
2. Pytest: versatile testing framework supporting unit, functional, and integration testing. Website: pytest.org
3. Behave: A behavior-driven development (BDD) framework. Website: https://behave.readthedocs.io

## References:

1. [Playwright - Python official page](https://playwright.dev/python/)
2. [Installation](https://playwright.dev/python/docs/intro)
3. [Assertion](https://playwright.dev/python/docs/test-assertions)


## Playwright Installation:

From Python point of view Playwright is just a package

Installation: 
```python
pip install pytest-playwright
```

## Playwright Launching:

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
Page Object Structure example: 
```python
# Import libraries
from playwright.sync_api import Page

# PO constructor (including locators)
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

    # Methods of PO
    # method to iteract with page
    def navigate(self, url: str):
        self.page.goto(url)
        self.currentAddressField.click()

    # method to get information
    def navigate(self, url: str):
        self.permanentAddressField.text_content()

    # Assertion methods
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
Assert methods are numerous:
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
- 'assert' returns Boolean
- 'expect' returns None

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

```python
    # Actions on page
    def navigate(self, url: str):
        self.page.goto(url)


    # Get information from page
    def check_loading_initial_page(self):
        return self.text_selenium.is_visible()
```

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

## Task Exercises:

Create PO and test-suit for page https://demoqa.com/text-box with following scenario
- Add data like:
```python
fullName = "Donald Duck";
email = "donald.duck@example.com";
currentAddress = "56 Main St";
permanentAddress = "379 Apple Rd";
```
- Click Submit button
- Check that data is displayed as expected

```
Name:Donald Duck
Email:donald.duck@example.com
Current Address :56 Main St
Permananet Address :379 Apple Rd
```
