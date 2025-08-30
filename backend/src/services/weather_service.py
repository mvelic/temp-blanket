# backend/src/services/weather_service.py
from os import getenv
import requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, wait_random
from models.data_models import TemperatureReading


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
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=3)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Open-Meteo API: {e}")
        return None
    
    return data


def parse_temp_readings(raw_api_data):
    """
    Parses the raw temperature api data into the TemperatureReading model
    """
    temp_data = []
    for date, temp in zip(raw_api_data.get("daily").get("time"), raw_api_data.get("daily").get("temperature_2m_max")):
        temp_data.append(TemperatureReading(reading_date=date, max_temp_c=temp))

    return temp_data
