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

Playwright supports all standart types of locators liek css or xpath. Additionally it provides the additional functionality like below:
1. Last and first locator lik
page.locator(.classname).last.click
2. Ability operate with locator in "#shadow-root"
Remark: #shadow-root is area within DOM. Locators within this section are not available for many Test Automation Frameworks
3. The numerous build-in methods like .to_have_text(). Expamle of code
 
```python
page.get_by_role("#Category")).to_have_text(["plates", "caps", "catleriese"])
```


### Playwright Assert vs Expect

The important part of playwright is 'expect'

'assert' returns Boolean

'expect' returns None

The main advantage of 'expect' - waiting for page loading with required parameter till framework's timer
