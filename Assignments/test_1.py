import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        result = 1 / 0
@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),       # Test case 1
    (1, 1, 2),       # Test case 2
    (-1, 1, 0),      # Test case 3
    (0, 0, 0)        # Test case 4
])
def test_addition(a, b, expected):
    assert a + b == expected, f"Expected {a} + {b} to be {expected}"

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 5),
    (1, 1, 2),
    (-1, 1, 0),
    (0, 0, 0)
], ids=["test_case_1", "test_case_2", "test_case_3", "test_case_4"])
def test_addition(a, b, expected):
    assert a + b == expected, f"Test failed: {a} + {b} should equal {expected}"

