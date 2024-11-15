# Topic 6: API Testing with Python

API Testing is a crucial component in test automation, ensuring that interactions between software components or systems meet specified requirements. This module will cover Python's tools and libraries for API testing, emphasizing HTTP requests, response validation, and creating automated API test suites.


## Learning Objectives

By the end of this module, you'll be able to:

1. Understand the basics of `RESTful` APIs and their significance in testing.
2. Use Python libraries like `requests` to interact with APIs.
3. Build test cases to validate API responses, status codes, and data formats.
4. Understand API authentication methods for testing secure endpoints.
5. Automate API testing using frameworks like pytest.

## Samples for API Testing

Check the folder `sample` to see a basic and an advanced API Testing.


## References

- [API Testing Best Practices](https://www.guru99.com/api-testing.html)
- [Requests Library Documentation](https://docs.python-requests.org/en/master/)
- [JSONPlaceholder - Free Fake API for Testing](https://jsonplaceholder.typicode.com/)
- [Swagger Petstore](https://petstore.swagger.io/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)

---


## Introduction to `RESTful` APIs and HTTP Methods

A `RESTful` API (**RE**presentational **S**tate **T**ransfer) enables communication over HTTP. REST APIs operate using standard HTTP methods:

- GET: Retrieve data
- POST: Create data
- PUT: Update data
- DELETE: Remove data


Let's identify open APIs and explore its endpoints by making basic GET and POST requests. For a more visual exploration, tools like [Postman](https://www.postman.com/downloads/) are highly useful:


### No Authentication Required

These APIs are useful for learning basic request structures without worrying about authentication.

- [JSONPlaceholder](https://jsonplaceholder.typicode.com): A simple REST API for testing HTTP requests with common CRUD operations.
- [Cat Facts](https://catfact.ninja): An API providing random cat facts, useful for testing basic GET requests.
- [CoinGecko API](https://www.coingecko.com/en/api): Accesses cryptocurrency data such as prices, market trends, and exchanges. It has a paid plan as well that may require other kind of authentication method.
- [Public APIs Directory](https://public-apis.io): Provides a vast list of public APIs across categories with no authentication requirements.


### API Key Authentication

These APIs require an API key, which is usually sent as a header or query parameter.

- [OpenWeatherMap](https://openweathermap.org/api): Offers weather and forecast data. Requires a free API key for most endpoints.
- [NASA APIs](https://api.nasa.gov): A suite of APIs offering data on space and Earth science (APOD, Earth, Mars Rover Photos). Requires an API key.
- [News API](https://newsapi.org): Provides recent news articles and headlines. Requires a free API key.
- [The Dog API](https://thedogapi.com): Returns random pictures and information about dog breeds. Requires an API key for certain endpoints.


### Bearer Token (OAuth 2.0)

APIs utilizing OAuth 2.0 for generating Bearer Tokens, often requiring user authorization flows.

- [GitHub API](https://docs.github.com/en/rest): Allows access to GitHub data such as repositories and user profiles via personal access tokens.
- [Spotify API](https://developer.spotify.com/documentation/web-api): Provides access to music data, playlists, and user information through an OAuth 2.0 flow for token generation.
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api): Offers access to Twitter data, including tweets and user information, requiring an OAuth 2.0 Bearer Token.


### Session-Based Authentication

Some APIs allow for sessions created via login credentials, with a token issued to authenticate subsequent requests.

- [Petstore Swagger API](https://petstore.swagger.io): A sample API for testing session-based workflows and user scenarios in Swagger.
- [ReqRes](https://reqres.in): A mock API simulating user CRUD operations and login/logout functionalities, ideal for session-based testing.


## Setting Up API Requests with the `requests` Library

The `requests` library is a popular Python library for sending HTTP requests and managing responses, including data handling in `JSON` format.


### Example

```python
import requests

# Sending a GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # Should print 200
print(response.json())       # Should print `JSON` response data
```


## Validating API Responses

When validating API responses, testers check the following:

- **Status Code:** Confirms if the request succeeded (e.g., `200 OK`, `404 Not Found`). See the list of status code available [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- **Response Time:** Measures how quickly the API responds.
- **Response Data:** Verifies correctness and data format (e.g., `JSON` structure and data types).


### Example

```python
def test_api_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert "userId" in response.json()
    assert isinstance(response.json()["id"], int)

test_api_response()
```


## `JSON` Manipulation (Serialize and Deserialize)

In API testing, `JSON` (JavaScript Object Notation) is a widely used data format for communication between clients and servers due to its simplicity and readability. `JSON` serialization is the process of converting Python objects into `JSON` format, while deserialization is the reverse, converting `JSON` data into Python objects.

The Python's `json` module provides methods to handle `JSON` data, including `json.dumps()` for serialization and `json.loads()` for deserialization.

### Example

- Serialize a Python Dictionary to JSON:

```python
import json

data = {"name": "Alice", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(json_data)  # Output: {"name": "Alice", "age": 30, "city": "New York"}
```

- Deserialize JSON to a Python Dictionary:

```python
import json

json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data["name"])  # Output: Alice
```


## Authentication and API Testing

Many APIs require authentication to access secured endpoints. Common methods include:

- **API Key:** A token-based method, often in headers or query parameters, suitable for quick access to APIs.
- **Bearer Token:** Used in OAuth 2.0 for secure access, added to headers as Authorization: Bearer <token>.
- **Basic Auth:** Combines a username and password, encoded in base64, used for simpler authentication.
- **OAuth 2.0:** An advanced authorization framework with grant types and token refresh options, ideal for third-party access.
- **Digest Authentication:** Similar to Basic Auth, but with hashing, adding security during transmission.
- **Session-Based Authentication:** Used in web apps, stores session ID in cookies.
- **JWT (JSON Web Tokens):** Stateless tokens encoding user details, suitable for distributed or serverless setups.
- **SAML:** XML-based SSO (Single Sign-On) method exchanging data between identity and service providers.


### Example

```python
# Basic authentication example
response = requests.get("https://api.example.com/secure-data", auth=("username", "password"))
print(response.json())

# Bearer token example
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
response = requests.get("https://api.example.com/secure-data", headers=headers)
print(response.json())
```


## Automating API Tests with `pytest`

`pytest` allows API test automation, making tests modular and reusable. Test functions can be organized with fixtures for efficient setup and data reuse.

Fixtures provide predefined configurations or states that tests can rely on. Fixtures are particularly useful when:
- You need consistent test environments (e.g., database states, configurations, test data)
- The setup is shared across multiple tests.


### Example

```python
import pytest
import requests

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/posts"

def test_get_request(base_url):
    response = requests.get(f"{base_url}/1")
    assert response.status_code == 200
    assert "title" in response.json()
```


## Handling Errors and Exception Management

Handling exceptions like timeouts and connection errors is essential to make tests resilient.


### Example

```python
try:
    response = requests.get("https://api.example.com/nonexistent")
    response.raise_for_status()  # Will raise an error for 4xx/5xx responses
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```


## Advanced API Testing Techniques

As APIs become more complex and integral to modern applications, testing them effectively requires more than just basic validations. Advanced API testing techniques enable testers to simulate real-world scenarios, isolate environments, ensure reliability, and uncover edge cases.

This section dives into sophisticated methodologies such as mocking responses, schema validation, testing asynchronous APIs, and more.


### Mocking API Responses

Mocking API responses can control the testing environment without making actual requests. Libraries like `responses` allow for mocking in Python.

Mocking is useful when:
- Testing interactions with external dependencies (e.g., APIs, databases).
- Isolating components to test specific logic.

Check out more about [mocking here](https://realpython.com/python-mock-library/#what-is-mocking)

The `patch` decorator (from the `unittest.mock` module) is used for temporarily replacing objects or methods.

```python
import requests
from unittest.mock import patch

@patch('requests.get') # Mocking the HTTP GET method
def test_mocked_get_request(mock_get): # The param `mock_get` is the `mock` object created by the `patch`
    """
    Configuring the `mock` object:
     - mock_get.return_value: Represents the mocked response object returned when `requests.get` is called.
     - status_code: Sets the HTTP status code of the mocked response to 200 (indicating success).
     - json.return_value: Simulates the JSON data returned by the mocked response, in this case, a dictionary with a single key-value pair: {"title": "Mocked Title"}.
    """

    mock_get.return_value.status_code = 200 #
    mock_get.return_value.json.return_value = {"title": "Mocked Title"}

    # The below line will call `requests.get` using the URL, but due to the `patch`,
    # the actual `requests.get` method is not executed and the test uses the mock object
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Mocked Title"
```

Fixtures can also be combined with mocking for powerful test setups. For example, you can define a fixture that provides a mocked API client for your tests:

```python
import pytest
from unittest.mock import patch

@pytest.fixture
def mocked_api_response():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"message": "Hello from fixture!"}
        yield mock_get

def test_api_with_fixture(mocked_api_response):
    response = requests.get("https://example.com/api")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello from fixture!"
```


**Note:**

Key Differences Between Mocks and Fixtures

| Feature     | Mocks                                              | Fixtures                                                         |
|-------------|----------------------------------------------------|------------------------------------------------------------------|
| Purpose     | Simulates external calls or object behavior        | Provides predefined setups and states for tests                  |
| Use Case    | Testing API interactions or external services      | Managing environment setups, dependencies, or reusable test data |
| Scope       | Focused on replacing specific behaviors or objects | Broader, managing the test's context or environment              |
| Reusability | Generally specific to a test or scenario           | Highly reusable across multiple tests                            |
| Example     | Mocking an API request to avoid real network calls | Providing a database connection or preloaded data for tests      |


### Contract Testing with Schema Validation

API responses should adhere to predefined contracts or schemas. You can use libraries like `jsonschema` or `pydantic` to validate response structures.

```python
from jsonschema import validate

# Define expected schema
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
    },
    "required": ["id", "title", "completed"]
}

# Example API response
response_data = {
    "id": 1,
    "title": "Test Task",
    "completed": True
}

# Validate response data against schema
def test_response_schema():
    validate(instance=response_data, schema=schema)
```


### Testing Asynchronous APIs

For APIs that use asynchronous programming, libraries like `pytest-asyncio` can be utilized to test the behavior of async endpoints.

```python
import pytest
import aiohttp

@pytest.mark.asyncio
async def test_async_api():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            assert response.status == 200
            json_data = await response.json()
            assert "title" in json_data
```


### Rate Limiting and Retry Mechanisms

Test how APIs handle rate limits and implement retries using libraries like `tenacity`.

```python
from tenacity import retry, wait_exponential, stop_after_attempt
import requests

@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(3))
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code != 200:
        raise Exception("Rate limit exceeded")
    return response.json()

def test_retry_mechanism():
    try:
        data = fetch_data()
        assert isinstance(data, list)
    except Exception as e:
        assert str(e) == "Rate limit exceeded"
```


### Security Testing

Test APIs against common vulnerabilities like SQL Injection, XSS, or improper authentication mechanisms.

```python
def test_header_injection():
    headers = {"Authorization": "Bearer invalid_token; DROP TABLE users;"}
    response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
    assert response.status_code == 401  # Expect unauthorized access
```


### Performance Testing with Load Tools

Use tools like `locust` or `pytest-benchmark` to simulate high loads and test API scalability.

```python
import requests

def test_performance(benchmark):
    def fetch():
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        assert response.status_code == 200

    benchmark(fetch)
```


### Data-Driven Testing

Use `@pytest.mark.parametrize` to test multiple data combinations, mimicking real-world scenarios.

```python
import pytest

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (9999, 404),
    (None, 400)
])
def test_user_api(user_id, expected_status):
    url = "https://jsonplaceholder.typicode.com/users"
    params = {"id": user_id} if user_id else {}
    response = requests.get(url, params=params)
    assert response.status_code == expected_status
```


### Dynamic Request Manipulation

Generate dynamic payloads for `POST` or `PUT` requests and test server behavior.

```python
import requests

def test_dynamic_post():
    payload = {
        "title": "Dynamic Title",
        "body": "Dynamic Body",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
```


### Dependency Injection for Reusability

Design reusable utilities to manage `setup`, `teardown`, and `dependency injections` for complex API scenarios.

```python
import pytest

@pytest.fixture
def api_client():
    class APIClient:
        def get(self, endpoint):
            return requests.get(f"https://jsonplaceholder.typicode.com{endpoint}")

        def post(self, endpoint, data):
            return requests.post(f"https://jsonplaceholder.typicode.com{endpoint}", json=data)

    return APIClient()

def test_api_client_get(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200
```
