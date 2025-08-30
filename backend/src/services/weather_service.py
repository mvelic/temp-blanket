# backend/src/services/weather_service.py
from os import getenv
import requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, wait_random
from ..models.data_models import TemperatureReading


load_dotenv()


@retry(stop=stop_after_attempt(5),
       wait=wait_exponential(multiplier=1.5, max=8)+wait_random(0, 2))
def get_historical_temperatures(latitude, longitude, year):
    """
    Fetches daily average temperatures for a given location and year.
    """
    url = f"https://{getenv("WEATHER_URL")}"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": f"{year}-01-01",
        "end_date": f"{year}-12-31",
        "daily": "temperature_2m_max",
        "timezone": "auto",
        "temperature_unit": "fahrenheit"
    }

    try:
        response = requests.get(url, params=params, timeout=3)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Open-Meteo API: {e}")
        return None
    
    return data


def parse_temp_readings(api_response):
    """
    Takes the api data and returns the parsed temp readings
    """
    if api_response:
        daily_max_temps = api_response.get("daily", {}).get("temperature_2m_max")
        dates = api_response.get("daily", {}).get("time")

        if dates and daily_max_temps:
            for date, temp in zip(dates, daily_max_temps):
                TemperatureReading(date, temp)