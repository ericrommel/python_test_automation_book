import json
import requests


# Base URL
BASE_URL = "https://jsonplaceholder.typicode.com"

# Authentication tokens for demonstration purposes
API_KEY = "your_api_key_here"
BEARER_TOKEN = "your_bearer_token_here"


# Test GET request
def test_get_request():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert "userId" in response.json()


# Test POST request with JSON data
def test_post_request():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/posts", json=payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"


# Test PUT request to update data
def test_put_request():
    payload = {"title": "updated title", "body": "updated body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


# Test DELETE request
def test_delete_request():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


# Test GET with API Key authentication (add the key as a query parameter)
def test_get_with_api_key():
    response = requests.get(f"{BASE_URL}/posts", params={"api_key": API_KEY})
    assert response.status_code == 200


# Test GET with Bearer Token authentication
def test_get_with_bearer_token():
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert response.status_code == 200


# Test GET with Basic Auth
def test_get_with_basic_auth():
    response = requests.get(f"{BASE_URL}/posts", auth=("username", "password"))
    assert response.status_code == 200


# Test for JSON serialization and deserialization
def test_json_serialization_deserialization():
    # Serialization
    data = {"name": "Alice", "age": 30, "city": "New York"}
    json_data = json.dumps(data)
    assert isinstance(json_data, str)

    # Deserialization
    deserialized_data = json.loads(json_data)
    assert deserialized_data["name"] == "Alice"
