# backend/src/services/weather_service.py
import requests

def get_historical_temperatures(latitude, longitude, start_date, end_date):
    """
    Fetches daily average temperatures for a given location and date range.
    """
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max",
        "timezone": "auto",
        "temperature_unit": "fahrenheit"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Open-Meteo API: {e}")
        return None

if __name__ == '__main__':
    # Example for San Francisco, 2024 (37.77, -122.42)
    # Washington DC (38.9072° N, 77.0369° W)
    sf_latitude = 38.91
    sf_longitude = -77.01
    start = "2024-01-01"
    end = "2024-12-31"

    temperature_data = get_historical_temperatures(sf_latitude, sf_longitude, start, end)

    if temperature_data:
        # Here's what the data looks like. You will parse it later.
        print(temperature_data)
        daily_max_temps = temperature_data.get("daily", {}).get("temperature_2m_max")
        dates = temperature_data.get("daily", {}).get("time")

        if dates and daily_max_temps:
            print("\nDates and Daily Max Temperatures:")
            for date, temp in zip(dates, daily_max_temps):
                print(f"{date}: {temp}°F")