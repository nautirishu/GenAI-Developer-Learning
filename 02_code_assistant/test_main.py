import pytest
from main import celsius_to_fahrenheit, calculate_factorial, odd_even

# ==========================================
# Celsius to Fahrenheit Tests
# ==========================================

def test_celsius_to_fahrenheit_positive():
    """Test 1: Check standard positive temperature conversion."""
    assert celsius_to_fahrenheit(25) == 77.0


def test_celsius_to_fahrenheit_freezing_and_negative():
    """Test 2: Check freezing point and sub-zero temperatures."""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(-40) == -40.0  # -40 is identical in both scales


# ==========================================
# Factorial Tests
# ==========================================

def test_factorial_standard_values():
    """Test 3: Check typical positive integers."""
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6


def test_factorial_zero_and_one():
    """Test 4: Check edge cases for 0! and 1! (both must return 1)."""
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1


def test_factorial_negative_error():
    """Test 5: Check that negative inputs raise a ValueError exception."""
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        calculate_factorial(-5)


# ==========================================
# Odd Even Tests
# ==========================================

def test_oddeven_standard_values():
    """Test 6 check odd even for normal positive or negative integers"""
    assert odd_even(4) == "Even"
    assert odd_even(5) == "Odd"
    assert odd_even(-3) == "Odd"
    assert odd_even(-8) == "Even"

def test_oddeven_Invalid_input():
    """test for invalid values"""
    with pytest.raises(TypeError):
        odd_even(5.2)