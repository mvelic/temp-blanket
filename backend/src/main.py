from services.input_service import verify_year
from services.weather_service import get_historical_temperatures


def main(latitude, longitude, year):
    temperature_data = get_historical_temperatures(latitude, longitude, year)

    verify_year(year)

    if temperature_data:
        # Here's what the data looks like. You will parse it later.
        # print(temperature_data)
        daily_max_temps = temperature_data.get("daily", {}).get("temperature_2m_max")
        dates = temperature_data.get("daily", {}).get("time")

        if dates and daily_max_temps:
            print("\nDates and Daily Max Temperatures:")
            for date, temp in zip(dates, daily_max_temps):
                print(f"{date}: {temp}°F")


if __name__ == '__main__':
    # Example for San Francisco, 2024 (37.77, -122.42)
    # Washington DC (38.9072° N, 77.0369° W)
    latitude = 38.91
    longitude = -77.01
    year = "1940"

    main(latitude, longitude, year)
