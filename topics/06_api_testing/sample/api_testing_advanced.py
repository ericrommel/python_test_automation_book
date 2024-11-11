import requests
import pytest

"""
-> Set Up and Obtain an API Key
- Go to the OpenWeatherMap API (https://openweathermap.org/api) and sign up for a free account.
- After logging in, navigate to the API keys section on your account page to generate a key (https://home.openweathermap.org/api_keys).
- Note your API key (let's call it API_KEY).
"""

# API Configuration
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_api_key_here"  # Replace with your actual API key


@pytest.fixture
def auth_params():
    """Fixture to provide authentication parameters."""
    return {"appid": API_KEY}


# Test API with Parameterized City Names
@pytest.mark.parametrize("city", ["London", "Paris", "New York", "Tokyo", "Sydney"])
def test_weather_for_city(auth_params, city):
    """Test that a city weather data can be fetched successfully."""
    params = {"q": city, **auth_params}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, f"Failed to fetch weather data for {city}"
    data = response.json()
    assert "weather" in data, "Response does not contain 'weather' information"
    assert "main" in data, "Response does not contain 'main' section for temperature and humidity"


# Test with Invalid API Key
def test_invalid_api_key():
    """Test that an invalid API key returns a 401 error."""
    params = {"q": "London", "appid": "invalid_key"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 401, "Expected a 401 Unauthorized error with an invalid API key"


# Test Skipping Based on Conditions (e.g., API might be down)
@pytest.mark.skip(reason="Skipping test as API server might be temporarily down")
def test_api_unavailable():
    """Skip test if the API server is known to be down for maintenance."""
    response = requests.get(BASE_URL, params={"q": "London", "appid": API_KEY})
    assert response.status_code == 200


# Testing for Exception Handling
def test_handle_api_error():
    """Test handling of connection errors gracefully."""
    with pytest.raises(requests.exceptions.ConnectionError):
        # Simulate a faulty URL to trigger a connection error
        requests.get("https://invalid-url.openweathermap.org", params={"q": "London", "appid": API_KEY})
