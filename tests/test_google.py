# tests/test_example.py

# A simple function to test.
def add(x, y):
    return x + y

# A simple function for subtraction.
def subtract(x, y):
    return x - y

# A test function that uses the `add` function.
def test_addition():
    """Test that the add function works correctly."""
    assert add(1, 1) == 2
    assert add(5, 0) == 5
    assert add(-1, 1) == 0

# You can add more test cases here.
def test_subtraction():
    """Test a hypothetical subtraction function."""
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
