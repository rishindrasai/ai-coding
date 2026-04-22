'''#task 1
def factorial(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result
print(factorial(5))
#Identify the error in the above code and correct it. The factorial of a number n is the product of all positive integers less than or equal to n. The loop should include n, so the range should be from 1 to n+1.explain the bug and the correction made.
''''''The error in the code is that the loop iterates from 1 to n-1, which means it does not include n in the calculation of the factorial. The factorial of a number n should include all positive integers up to and including n.
To correct this, the range in the loop should be changed to range(1, n+1) so that it includes n in the calculation. This way, the function will correctly compute the factorial of n by multiplying all integers from 1 to n.''''''
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial(5))
print(factorial(0))
#task 2
def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        return a / b
print(calc(10, 5, "add"))  # Output: 15
print(calc(10, 5, "sub"))  # Output: 5
print(calc(10, 5, "mul"))  # Output: 50
print(calc(10, 5, "div"))  # Output: 2.0
#fix the above code to handle division by zero error. If b is zero and c is "div", the function should return "Error: Division by zero". include docstring with proper description of the function and its parameters.
def calc(a, b, c):
    """
    Perform basic arithmetic operations based on the operator provided.

    Parameters:
    a (float): The first number.
    b (float): The second number.
    c (str): The operation to perform. It can be "add", "sub", "mul", or "div".

    Returns:
    float or str: The result of the arithmetic operation or an error message for division by zero.
    """
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        if b == 0:
            return "Error: Division by zero"
        else:
            return a / b
print(calc(10, 5, "add"))  # Output: 15
print(calc(10, 5, "sub"))  # Output: 5
print(calc(10, 5, "mul"))  # Output: 50
print(calc(10, 0, "div"))  # Output: Error: Division by zero  
#task 3
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
print(Checkprime(7))  # Output: True
print(Checkprime(10))  # Output: False
print(Checkprime(1))  # Output: True (Incorrect, should be False)
#Identify the error in the above code and correct it. The function is not correctly checking for prime numbers because it returns True after the first iteration of the loop, which is incorrect. The return statement should be outside the loop to ensure that all possible divisors are checked before determining if the number is prime or not.list all the PEP8 violations and refactor the code
def check_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 
print(check_prime(7))  # Output: True
print(check_prime(10))  # Output: False
print(check_prime(1))  # Output: False
#task 4
#In a GitHub project, a teammate submits:
def processData(d):
    return [x * 2 for x in d if x % 2 == 0]
print(processData([1, 2, 3, 4, 5]))  # Output: [4, 8]
#better naming and function purpose clarity. review the readability, naming , reusability,modularity and edge cases likr non-list input and empty list and non-integer elements in the list. The function name 'processData' is not descriptive of what the function does. A better name would be 'double_even_numbers', which clearly indicates that the function doubles the even numbers in the input list. Additionally, the function should include error handling for edge cases such as non-list input, empty lists, and non-integer elements in the list to improve its robustness and usability.
def double_even_numbers(data):
    """
    Double the even numbers in the input list.

    Parameters:
    data (list): A list of integers to process.

    Returns:
    list: A list containing the doubled values of the even numbers from the input list.

    Raises:
    TypeError: If the input is not a list or contains non-integer elements.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    
    result = []
    for x in data:
        if not isinstance(x, int):
            raise TypeError("All elements in the list must be integers.")
        if x % 2 == 0:
            result.append(x * 2)
    
    return result
print(double_even_numbers([1, 2, 3, 4, 5]))  # Output: [4, 8]
print(double_even_numbers([]))  # Output: []
print(double_even_numbers([1, 3, 5]))  # Output: []
try:    print(double_even_numbers("not a list"))  # Should raise TypeError
except TypeError as e:    print(e)  # Output: Input must be a list.
try:    print(double_even_numbers([1, 2, "three", 4]))  # Should raise TypeError
except TypeError as e:    print(e)  # Output: All elements in the list must be integers.'''
#task 5
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
print(sum_of_squares([1, 2, 3]))  # Output: 14
print(sum_of_squares([100000,200000,400000]))  # Output: 2.1e+11
#identify the error and analyze time complexity of the above code. The error in the above code is that it does not handle large numbers efficiently, as it may lead to overflow when calculating the squares of large numbers. The time complexity of the above code is O(n), where n is the number of elements in the input list 'numbers', because it iterates through each element once to calculate the sum of squares.optimized version of the function to handle large numbers without overflow by using a more efficient approach, such as using a generator expression to calculate the squares and summing them up without storing intermediate results in memory.discuss trade offs between readability and performance
def sum_of_squares(numbers):
    return sum(num ** 2 for num in numbers)
print(sum_of_squares([1, 2, 3]))  # Output: 14
print(sum_of_squares([100000, 200000, 400000]))  # Output: 2.1e+11




