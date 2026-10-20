import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=Chennai"

def fetch_data():
    try:
        print(f"Fetching data from WeatherStack API for New York...")
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        print("API request successful. Data received:")
        return response.json()  # Return the JSON data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        raise


def mock_fetch_data():
    # This function simulates fetching data from the WeatherStack API without making an actual request.
    print("Mock fetching data from WeatherStack API for New York...")
    mock_response = {
        "request": {
            "type": "City",
            "query": "New York, United States of America",
            "language": "en",
            "unit": "m"
        },
        "location": {
            "name": "New York",
            "country": "United States of America",
            "region": "New York",
            "lat": "40.714",
            "lon": "-74.006",
            "timezone_id": "America/New_York",
            "localtime": "2024-06-01 12:00",
            "localtime_epoch": 1712102400,
            "utc_offset": "-4.0"
        },
        "current": {
            "temperature": 25,
            "weather_descriptions": ["Partly cloudy"],
            "wind_speed": 10,
            "humidity": 60
        }
    }
    print("Mock API request successful. Data received:")
    return mock_response