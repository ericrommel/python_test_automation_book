import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # take environment variables from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_test_plan(scenario: str) -> str:
    if not client.api_key:
        raise ValueError("OpenAI API key not found. Set it as an environment variable: 'OPENAI_API_KEY'.")

    prompt = f"Generate a test plan for the following test scenario:\n\n{scenario}"

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a detailed test plan for the following scenario: {test_scenario}",
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=100,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except openai.APIConnectionError as e:  # Handle API connection issues
        return f"Error: Unable to connect to the OpenAI API. Details: {e.__cause__}"
    except openai.RateLimitError:  # Handle rate limits
        return "Error: Rate limit exceeded. Please wait and try again later."
    except openai.APIStatusError as e:  # Handle general API status errors
        return f"Error: API returned a non-success status code {e.status_code}. Details: {e.response}"
    except openai.APIError as e:  # Catch all other API errors
        return f"An unexpected API error occurred: {str(e)}"
    except Exception as e:  # Handle any other exceptions
        return f"An unexpected error occurred: {str(e)}"


# Example usage:
test_scenario = "Test the login functionality of a website."
print(generate_test_plan(test_scenario))
