# tests/test_example.py

# A simple function to test.
def add(x, y):
    return x + y

# A test function that uses the `add` function.
def test_addition():
    """Test that the add function works correctly."""
    assert add(1, 1) == 2
    assert add(5, 0) == 5
    assert add(-1, 1) == 0

# You can add more test cases here.
def test_subtraction():
    """Test a hypothetical subtraction function."""
    # This test will fail if a subtraction function isn't defined or isn't correct,
    # demonstrating how a failing test appears.
    # assert 5 - 2 == 3
    pass # This 'pass' is used to make the test function valid but not actually test anything.
