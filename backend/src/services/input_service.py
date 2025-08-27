# backend/src/services/input_service.py
from datetime import datetime


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
