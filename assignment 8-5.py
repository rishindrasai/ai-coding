"""#task 1
def is_valid_username(username):
  
    if not isinstance(username, str):
        return False
    
    if len(username) < 5 or len(username) > 15:
        return False
    
    if username[0].isdigit():
        return False
    
    if ' ' in username:
        return False
    
    if not username.isalnum():
        return False
    
    return True


# Test cases
assert is_valid_username("user123") == True
assert is_valid_username("john") == False  # Too short
assert is_valid_username("thisismyverylongusername") == False  # Too long
assert is_valid_username("123user") == False  # Starts with digit
assert is_valid_username("user 123") == False  # Contains space
assert is_valid_username("user@123") == False  # Contains special character
assert is_valid_username("User_123") == False  # Contains underscore
assert is_valid_username("validUser99") == True
assert is_valid_username("A") == False  # Too short
assert is_valid_username("abcde") == True

print("All tests passed!")

#task 2
def classify_value(value):
   
    if not isinstance(value, int) or isinstance(value, bool):
        return "Invalid Input"
    
    if value == 0:
        return "Zero"
    elif value % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test cases
assert classify_value(4) == "Even"
assert classify_value(7) == "Odd"
assert classify_value(0) == "Zero"
assert classify_value(-2) == "Even"
assert classify_value(-3) == "Odd"
assert classify_value("10") == "Invalid Input"
assert classify_value(3.5) == "Invalid Input"
assert classify_value(None) == "Invalid Input"
assert classify_value(True) == "Invalid Input"

print("All task 2 tests passed!")

#task 3
def is_palindrome(s):
    if not isinstance(s, str):
        return False
    
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# Test cases
assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("A man a plan a canal Panama") == True
assert is_palindrome("noon") == True
assert is_palindrome("python") == False
assert is_palindrome("a") == True
assert is_palindrome("") == True
assert is_palindrome(123) == False
assert is_palindrome("Was it a car or a cat I saw") == True

print("All task 3 tests passed!")"""

#doc test
import doctest
def add(a, b):
    """
    Add two numbers and return the result.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 5)
    5
    >>> add(3.5, 1.5)
    5.0
    >>> add(-2, -3)
    -5
    """
    return a + b


if __name__ == "__main__":
    doctest.testmod()