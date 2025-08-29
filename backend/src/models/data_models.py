# backend/src/models/data_models.py
from datetime import date
from enum import Enum
# from typing import List, Dict
from pydantic import BaseModel, computed_field


class TemperatureScale(Enum):
    C = "Celcius"
    F = "Fahrenheit"


class City(BaseModel):
    """Represents a city's basic data"""
    city_name: str
    latitude: float
    longitude: float


class TemperatureReading(BaseModel):
    """Represents a single day's temperature data"""
    reading_date: date
    max_temp_c: float

    @computed_field
    @property
    def max_temp_f(self) -> int:
        return _convert_to_f(self.max_temp_c)


class ColorAssignment(BaseModel):
    """Represents the data model for the user's color assignments"""
    upper_temp_c: float
    lower_temp_c: float
    scale: TemperatureScale
    hex_color: str

    @computed_field
    @property
    def upper_temp_f(self) -> int:
        return _convert_to_f(self.max_temp_c)

    @computed_field
    @property
    def lower_temp_f(self) -> int:
        return _convert_to_f(self.min_temp_c)


# class ProcessedTemperatureData(BaseModel):
#     """Represents the final processed data to be sent to the frontend"""
#     temps_colors: List[Dict{"Temp": TemperatureReading, "Color": ColorAssignment}]


class TemperatureBlanket(BaseModel):
    """ Processed user request data """
    city: City
    year: int
    # data: ProcessedTemperatureData
    # historical_temps: List[TemperatureReading]
    # color_assignments: List[ColorAssignment]


def _convert_to_f(temp_c) -> int:
    """Converts Celcius to Fahrenheit"""
    return int((9/5 * temp_c) + 32)
