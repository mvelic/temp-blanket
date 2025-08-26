from datetime import datetime

import pytest
from src.services.weather_service import verify_year


prior_year = datetime.now().year - 1


def test_verify_year():
    assert verify_year("1939") == f"Please select a year between 1940 and {str(prior_year)}."
    assert verify_year("1940") == "1940"
    assert verify_year("2024") == "2024"
    assert verify_year("2025") == f"Please select a year between 1940 and {str(prior_year)}."