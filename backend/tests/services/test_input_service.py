# backend/tests/services/test_input_service.py
from datetime import datetime

import pytest
from src.services.input_service import verify_year


prior_year = datetime.now().year - 1


def test_verify_year():
    assert verify_year(None)    == f"Please enter a valid 4-digit year."
    assert verify_year("     ") == f"Please enter a valid 4-digit year."
    assert verify_year("alpha") == f"Please enter a valid 4-digit year."
    assert verify_year("4lph4") == f"Please enter a valid 4-digit year."
    assert verify_year("1939")  == f"Please enter a year between 1940 and {str(prior_year)}."
    assert verify_year("1940")  == f"1940"
    assert verify_year("2024")  == f"2024"
    assert verify_year("2025")  == f"Please enter a year between 1940 and {str(prior_year)}."