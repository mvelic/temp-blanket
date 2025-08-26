# backend/src/services/weather_service.py
from datetime import datetime
import requests
from tenacity import retry, stop_after_attempt, wait_exponential, wait_random


@retry(stop=stop_after_attempt(5),
       wait=wait_exponential(multiplier=1.5, max=8)+wait_random(0, 2))
def get_historical_temperatures(latitude, longitude, year):
    """
    Fetches daily average temperatures for a given location and year.
    """
    verify_year(year)
    
    url = "https://archive-api.open-meteo.com/v1/archive"
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


def verify_year(year):
    """
    Verifies that the year provided falls between 1940 and the prior year.
    """
    oldest_year = 1940
    prior_year = datetime.now().year - 1

    if int(year) < oldest_year or int(year) > prior_year:
        return f"Please select a year between 1940 and {str(prior_year)}."
    return year


if __name__ == '__main__':
    # Example for San Francisco, 2024 (37.77, -122.42)
    # Washington DC (38.9072° N, 77.0369° W)
    latitude = 38.91
    longitude = -77.01
    year = "1940"

    temperature_data = get_historical_temperatures(latitude, longitude, year)

    if temperature_data:
        # Here's what the data looks like. You will parse it later.
        print(temperature_data)
        daily_max_temps = temperature_data.get("daily", {}).get("temperature_2m_max")
        dates = temperature_data.get("daily", {}).get("time")

        if dates and daily_max_temps:
            print("\nDates and Daily Max Temperatures:")
            for date, temp in zip(dates, daily_max_temps):
                print(f"{date}: {temp}°F")