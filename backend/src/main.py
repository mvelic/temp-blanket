from services.input_service import verify_year
from services.weather_service import get_historical_temperatures, parse_temp_readings


def main(latitude, longitude, year):
    verify_year(year)
    api_temp_data = get_historical_temperatures(latitude, longitude, year)
    parsed_temp_data = parse_temp_readings(api_temp_data)
    print(parsed_temp_data)


if __name__ == '__main__':
    # Example for San Francisco, 2024 (37.77, -122.42)
    # Washington DC (38.9072° N, 77.0369° W)
    latitude = 38.91
    longitude = -77.01
    year = "1940"

    main(latitude, longitude, year)
