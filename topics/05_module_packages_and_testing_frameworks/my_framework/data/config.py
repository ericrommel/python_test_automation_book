import json
import os


class Config:
    BASE_URL = "https://the-internet.herokuapp.com"

    @staticmethod
    def get_test_data():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "test_data.json")
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Test data file not found at {file_path}")
