from unittest.mock import Mock
'''
# Mocking a function
mock_function = Mock(return_value=42)

# Call the mock function
result = mock_function()

# Assertions
assert result == 42
mock_function.assert_called_once()'''

#2
'''class Calculator:
    def add(self, a, b):
        return a + b

# Mock the add method
calculator = Calculator()
calculator.add = Mock(return_value=100)

# Call the mocked method
result = calculator.add(2, 3)

# Assertions
assert result == 100
calculator.add.assert_called_once_with(2, 3)  # Ensure it was called with specific arguments'''

#3
def process_payment(payment_gateway, amount):
    response = payment_gateway.charge(amount)
    if response.get("status") == "success":
        return "Payment Successful"
    else:
        return "Payment Failed"

# Test for process_payment function
def test_process_payment():
    # Create a mock object for the payment gateway
    mock_payment_gateway = Mock()

    # Simulate the behavior of the `charge` method
    mock_payment_gateway.charge.return_value = {"status": "success", "transaction_id": "12345"}

    # Test successful payment
    result = process_payment(mock_payment_gateway, 100)
    assert result == "Payment Successful"

    # Verify that the `charge` method was called with the correct amount
    mock_payment_gateway.charge.assert_called_once_with(100)

    # Simulate a failed payment
    mock_payment_gateway.charge.return_value = {"status": "failed", "error": "Insufficient funds"}

    # Test failed payment
    result = process_payment(mock_payment_gateway, 50)
    assert result == "Payment Failed"

    # Verify that the `charge` method was called again with the new amount
    mock_payment_gateway.charge.assert_called_with(50)

# Run the test
if __name__ == "__main__":
    test_process_payment()
    print("All tests passed!")