from DayOne import how_many_increments, create_sliding_window
import pytest

@pytest.mark.parametrize("test_input,expected", [ ([1,2], 1), ([2,1], 0), ([1,1], 0), ([500,500,500,500,500,499,500], 1) ] ) 
def test_how_many_increments(test_input, expected):
    assert how_many_increments(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [ ([1,2,3], [6]), ([2,1], None), ([1,2,3,4,5,6,7], [6,9,12,15,18]) ] )
def test_create_slinding_window(test_input, expected):
    assert create_sliding_window(test_input) == expected
