# Topic 6: API Testing with Python

API Testing is a crucial component in test automation, ensuring that interactions between software components or systems meet specified requirements. This module will cover Python's tools and libraries for API testing, emphasizing HTTP requests, response validation, and creating automated API test suites.


## Learning Objectives

By the end of this module, you'll be able to:

1. Understand the basics of `RESTful` APIs and their significance in testing.
2. Use Python libraries like `requests` to interact with APIs.
3. Build test cases to validate API responses, status codes, and data formats.
4. Understand API authentication methods for testing secure endpoints.
5. Automate API testing using frameworks like pytest.


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


## Advanced Testing Techniques - Mocking API Responses

Mocking API responses can control the testing environment without making actual requests. Libraries like responses allow for mocking in Python.


### Example

```python
import requests
from unittest.mock import patch

@patch('requests.get')
def test_mocked_get_request(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"title": "Mocked Title"}

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Mocked Title"
```
