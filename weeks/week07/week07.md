# Week 7: Web Automation with Playwright

## Playwright general information:
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

## Installation:
From Python point of view Playwright is just a package

Installation: 
```python
pip install pytest-playwright
```

## Launching:
From Python point of view Playwright is enhanced pytest

Launching: 
```python
pytest
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

## Assert vs Expect
The important part of playwright is 'expect'
'assert' returns Boolean
'expect' returns None
The main advantage of 'expect' - waiting for page loading with required parameter till framework's timer
