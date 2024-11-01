# Week 7: Web Automation with Playwright

## Summary:
Playwright is the powerful tool for Web Test automation (UI and API) in different programming languages:
- TypeScript, 
- JavaScript,
- .NET,
- Java.
- Python

It is 
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
3. [Pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html#autouse-fixtures-fixtures-you-don-t-have-to-request)

## Playwright and Pytest:
From Python point of view Playwright is enhanced Pytest Automation framework

### Pytest:
1. Focus on Test Functions: Primarily focuses on running test functions, managing test configurations, and handling test fixtures.
2. Testing Framework: Pytest is a general-purpose testing framework for Python that supports unit testing, integration testing, and end-to-end testing.
3. Fixture - kind of decorator allowы creating interaction between methods of test application 

### Playwright:
1. Targeted for UI Testing: Best suited for simulating and verifying real user interactions within a web interface.
2. Browser Automation Framework: Playwright is specifically designed for end-to-end web application testing and automates browser interactions (clicks, form filling, navigation, etc.).
3. Supports Multiple Browsers: Can control Chromium, Firefox, and WebKit (Safari) browsers, providing cross-browser testing capabilities.

## Installation:
From Python point of view Playwright is just a package

Installation: 
```python
pip install pytest-playwright
```

## Launching:

The simplest launching command: 
```python
pytest filename_with_pytest_playwright_code.py
```

## Test:
1. Action
2. Assertion
3. Using fixtures

## UI testing
Kernel of Playwright UI test: import Page

```python
from playwright.sync_api import Page
```
## API testing
[Playwright - API testing official documentation]([https://playwright.dev/python](https://playwright.dev/python/docs/api-testing)/)
[Playwright - API request-new-context]([https://playwright.dev/python](https://playwright.dev/python/docs/api-testing)/)

Kernel of  Playwright API test: import APIRequestContext

```python
import pytest
from playwright.sync_api import Playwright, APIRequestContext
..
@pytest.fixture(scope="session")
def api_request_context(Playwright):
    headers = {
        "Content-Type": "application/json"
    }
    request_context = playwright.request.new_context(
        base_url="https://server.com", extra_http_headers=headers
    )
    return request_context

def test_get_subpage(api_request_context: APIRequestContext)
    subpage = api_request_context.get(
        "/subpage"
    )

    assert subpage.ok
    assert subpage.status == 200:
```

## Playwright Assert vs Expect
The important part of playwright is 'expect'
'assert' returns Boolean
'expect' returns None
The main advantage of 'expect' - waiting for page loading with required parameter till framework's timer
