from services.input_service import verify_year, verify_city
from services.weather_service import get_historical_temperatures, parse_temp_readings


def main(city_name, year):
    verify_year(year)
    city = verify_city(city_name)
    print(type(city))
    print(city)
    # api_temp_data = get_historical_temperatures(city.get("latitude"), city.get("longitude"), year)
    # parsed_temp_data = parse_temp_readings(api_temp_data)
    # print(parsed_temp_data)


if __name__ == '__main__':
    city_name = "Washington DC"
    year = "1940"

    main(city_name, year)
