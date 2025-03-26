# from unittest.mock import Mock
#
# # Mocking a function
# mock_function = Mock(return_value=42)
#
# # Call the mock function
# result = mock_function()
#
# # Assertions
# assert result == 42
# mock_function.assert_called_once()  # Ensure it was called once
# from unittest.mock import Mock
#
# class Calculator:
#     def add(self, a, b):
#         return a + b
#
# # Mock the add method
# calculator = Calculator()
# calculator.add = Mock(return_value=10)
#
# # Call the mocked method
# result = calculator.add(2, 3)

# Assertions
# assert result == 10
# calculator.add.assert_called_once_with(2, 3)
import math

def test_float_comparison():
    result = math.sqrt(16)
    assert math.isclose(result, 4.0, rel_tol=1e-9), "Square root of 16 should be 4.0"
test_float_comparison()