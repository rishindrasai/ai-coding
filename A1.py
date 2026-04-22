#Create a Python program to take a string from the user and print the reversed string without using any functions.
'''
user_input = input("Enter a string: ")
reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
'''

#Optimize the Python string reversal code.Remove extra variables, simplify the loop logic, and make the code easy for others to read and understand
user_input = input("Enter a string: ")
reversed_string = ''.join(reversed(user_input))
print("Reversed string:", reversed_string)


#Create a Python program using a user-defined function to reverse a string.The function should return the reversed string.Add clear and meaningful comments so the code is easy to understand.
'''
def reverse_string(input_string):
    """
    This function takes a string as input and returns the reversed string.
    
    Args:
        input_string (str): The string to be reversed.

    Returns:

        str: The reversed string.    """
    reversed_str = ''   
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str
# Get user input
user_input = input("Enter a string: ")
# Call the function and display the result
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)
'''

#Compare the Python programs for string reversal written without functions and with functions.Analyze which one is better in terms of code clarity, reusability, ease of debugging, and use in large applications Provide a short report or table showing the comparisoM
'''
# Program without functions
user_input = input("Enter a string: ")
reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)  
# Program with functions
def reverse_string(input_string):
    """
    This function takes a string as input and returns the reversed string.
    
    Args:
        input_string (str): The string to be reversed.
    Returns:
        str: The reversed string.   
    """
    reversed_str = ''   
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str
# Get user input
user_input = input("Enter a string: ")
# Call the function and display the result
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)
'''

#Generate two Python programs to reverse a string:1. Using a loop (iterative approach) 2. Using Python built-in features or slicing .Compare them by explaining how they work, their time complexity, performance for large inputs, and when each approach should be used.
'''
# Iterative approach using a loop
def reverse_string_iterative(input_string): 
    """
    This function reverses a string using an iterative approach.
    
    Args:
        input_string (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    reversed_str = ''
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string_iterative("hello"))  # Output: "olleh"
# Built-in features using slicing
def reverse_string_slicing(input_string):

    """
    This function reverses a string using Python's slicing feature.
    
    Args:
        input_string (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_string[::-1]
print(reverse_string_slicing("hello"))  # Output: "olleh"
# Comparison:
# Both functions reverse a string but use different methods.
# The iterative approach builds the reversed string character by character, while the slicing method leverages Python's built-in capabilities for a more concise solution.
# Time Complexity: Both approaches have a time complexity of O(n), where n is the length of the string.
# Performance: The slicing method is generally faster and more efficient for large inputs due to its optimized
# implementation in Python.
# Usage: Use the iterative approach when you need more control over the reversal process or when working
# in environments where built-in features are limited. Use the slicing method for simplicity and performance in most cases.
'''