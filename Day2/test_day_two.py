from DayTwo import *
import pytest

@pytest.mark.parametrize("test_input, expected", [ ([["forward",5]], (5,0) ), ([["forward",0]], (0,0) ) ] )
def test_calculate_position(test_input, expected):
    assert calculate_position(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [ ([["forward",5]], (5,0) ), ([["forward",0]], (0,0) ) ] )
def test_calculate_position_two(test_input, expected):
    assert calculate_position_two(test_input) == expected