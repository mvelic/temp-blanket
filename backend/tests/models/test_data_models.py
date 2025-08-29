# backend/tests/models/test_data_models.py

import pytest
from src.models.data_models import _convert_to_f


def test_convert_to_f():
    assert _convert_to_f(-20.6) == -5
    assert _convert_to_f(-12.3) == 9
    assert _convert_to_f(0)     == 32
    assert _convert_to_f(17.6)  == 63
