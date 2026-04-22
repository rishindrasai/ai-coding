import pytest

"""import doctest

def add(a, b):
    """"""
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0, 0)
        0
        >>> add(10.5, 20.5)
        31.0
        >>> add(-5, -3)
        -8
    """""""
    return a + b


if __name__ == "__main__":
    doctest.testmod()"""

#pytest
import pytest
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-5, -3) == -8

def test_add_mixed_numbers():
    assert add(-1, 1) == 0

def test_add_zeros():
    assert add(0, 0) == 0

def test_add_floats():
    assert add(10.5, 20.5) == 31.0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])