# Import pytest framework from writing test cases
import pytest

# Import all functions from math_utils module
# This allows to test each functionality individually
from app.math_utils import (add, subtract, multiply, divide, floor_divide, modulus, power, absolute)

def test_add():
    # Test normal addition
    assert add(2, 3) == 5

def test_add_negative():
    # Ensures that incorrect result is not returned
    assert add (2, 2) != 5

def test_add_not_equal():
    # Ensure that incorrect result is not returned
    assert add(2, 2) != 5
    
def test_add_type():
    # Check return type is integer
    assert isinstance(add(2,3), int)
    
@pytest.fixture
def sample_numbers():
    # Fixtures provides reuseable test data
    return (10, 5)

def test_add_with_fixture(sample_numbers):
    # Using fixture values
    a, b = sample_numbers
    assert add(a, b) == 15

@pytest.mark.parametrize("a, b, result", [
    (1, 2, 3), (2, 3, 5), (10, 5, 15)
])
def test_add_parameterized(a, b, result):
    # Runs same test with multiple inputs
    assert add(a, b) == result
    
def test_subtract():
    # Test subtraction
    assert subtract(5, 2) == 3


def test_subtract_negative():
    # Test subtraction with negatives
    assert subtract(-5, -2) == -3
    
def test_multiply():
    # Test multiplication
    assert multiply(3, 4) == 12


def test_multiply_zero():
    # Any number multiplied by 0 should be 0
    assert multiply(5, 0) == 0
    
def test_divide():
    # Test normal division
    assert divide(10, 2) == 5


def test_divide_float():
    # Division should return float
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    # Test division by zero raises error
    with pytest.raises(ValueError):
        divide(10, 0)

def test_floor_divide():
    # Floor division removes decimal part
    assert floor_divide(7, 2) == 3


def test_floor_divide_negative():
    # Floor division with negative numbers
    assert floor_divide(-7, 2) == -4


def test_floor_divide_by_zero():
    # Should raise error when dividing by zero
    with pytest.raises(ValueError):
        floor_divide(10, 0)
        
def test_modulus():
    # Test remainder calculation
    assert modulus(7, 2) == 1


def test_modulus_zero():
    # 0 % number should be 0
    assert modulus(0, 5) == 0


def test_modulus_by_zero():
    # Modulus by zero should raise error
    with pytest.raises(ValueError):
        modulus(10, 0)
        
def test_power():
    # Test exponentiation
    assert power(2, 3) == 8


def test_power_zero():
    # Any number power 0 = 1
    assert power(5, 0) == 1
    
def test_absolute_positive():
    # Positive number remains same
    assert absolute(5) == 5


def test_absolute_negative():
    # Negative becomes positive
    assert absolute(-5) == 5


def test_absolute_zero():
    # Absolute of zero is zero
    assert absolute(0) == 0