
'''Refactor the given poorly structured Python script into a clean, modular, and reusable implementation.'''
# Harshad Number Checker (Unstructured Version)

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    temp = temp // 10

if sum_digits != 0:
    if num % sum_digits == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
'''Refactor into is_harshad(n) function with docstring and improved readability.'''
def is_harshad(n):
    """
    Check if a number is a Harshad number.

    A Harshad number is an integer that is divisible by the sum of its digits.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is a Harshad number, False otherwise.
    """
    temp = n
    sum_digits = 0

    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        temp //= 10

    if sum_digits == 0:
        return False

    return n % sum_digits == 0
# Example usage
num = int(input("Enter a number: "))

if is_harshad(num):
    print("True")
else:
    print("False")
    
