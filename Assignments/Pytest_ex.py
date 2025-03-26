#to run in terminal
#pytest test_example.py
#to run a particular test case


#let he file name has 'test' prefix
#test_filename.py
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        result = 1 / 0