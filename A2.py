# generate a program to calculate the sum of odd and even numbers in a list
'''def sum_odd_even(numbers):
    """
    Calculate the sum of odd and even numbers in a list.
    
    Args:
        numbers (list): A list of integers.
        
    Returns:
        tuple: A tuple containing the sum of even numbers and the sum of odd numbers.
    """
    sum_even = 0
    sum_odd = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return sum_even, sum_odd
print("Area Calculator for Different Shapes")   
'''

"""
Area Calculator for Different Shapes
This program demonstrates how to calculate the area of various geometric shapes.
"""
#"""Scenario: You are onboarding a junior developer. explain a function that calculates the area of different shapes.  Expected Output:  Code  Explanation"""
'''def calculate_area(shape: str, dimensions: tuple) -> float:
    """
    Calculate the area of different geometric shapes.
    
    Args:
        shape (str): The type of shape ('circle', 'rectangle', 'triangle').
        dimensions (tuple): The dimensions required to calculate the area.
            - For 'circle': (radius,)
            - For 'rectangle': (length, width)
            - For 'triangle': (base, height)
    
    Returns:
        float: The area of the shape.
    """
    import math
    if shape == 'circle':
        radius, = dimensions
        return math.pi * radius ** 2
    elif shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")
# Example usage
print("Area of Circle with radius 5:", calculate_area('circle', (5,)))          # Expected: 78.53981633974483
print("Area of Rectangle with length 4 and width 6:", calculate_area('rectangle', (4, 6)))  # Expected: 24
print("Area of Triangle with base 3 and height 7:", calculate_area('triangle', (3, 7)))      # Expected: 10.5
'''

#You are onboarding a junior developer. explain a function that calculates the area of different shapes.  Expected Output:  Code  Explanation

