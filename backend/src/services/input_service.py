# backend/src/services/input_service.py
from datetime import datetime
from models.data_models import City


def verify_year(year):
    """
    Verifies that the year provided falls between 1940 and the prior year.
    """
    oldest_year = 1940
    prior_year = datetime.now().year - 1

    if year is None or year.isalpha() or year.isspace():
        return f"Please enter a valid 4-digit year."
    
    try:
        if int(year) < oldest_year or int(year) > prior_year:
            return f"Please enter a year between 1940 and {str(prior_year)}."
        return year
    except ValueError:
        return f"Please enter a valid 4-digit year."


def verify_city(city_name):
    """
    Verifies a city and creates a City model
    """
    # Example for San Francisco (37.77, -122.42)
    # Washington DC (38.9072, -77.0369)
    lat  = 38.9072
    long = -77.0369

    try:
        city = City(city=city_name, latitude=lat, longitude=long)
        return city
    except ValueError:
        return f"This city does not exist."
