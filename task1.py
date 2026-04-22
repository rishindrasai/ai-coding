'''
refactor a given Python script that contains multiple repeated code blocks.
• Instructions:
o Prompt AI to identify duplicate logic and replace it with functions or classes.
o Ensure the refactored code maintains the same output.
o Add docstrings to all functions.
• Sample Legacy Code:
# Legacy script with repeated logic
print("Area of Rectangle:", 5 * 10)
print("Perimeter of Rectangle:", 2 * (5 + 10))
 
print("Area of Rectangle:", 7 * 12)
print("Perimeter of Rectangle:", 2 * (7 + 12))
 
print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))
'''
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width   
def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle.
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    Returns:
    float: The perimeter of the rectangle.
    """
    return 2 * (length + width)
# Example usage
rectangles = [(5, 10), (7, 12), (10, 15)]
for length, width in rectangles:
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"Area of Rectangle: {area}")
    print(f"Perimeter of Rectangle: {perimeter}")