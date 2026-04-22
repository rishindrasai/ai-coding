'''
refactor procedural input–processing logic into functions.
Instructions:
o Identify input, processing, and output sections.
o Convert each into a separate function.
o Improve code readability without changing behavior.
• Sample Legacy Code:
num = int(input("Enter number: "))
square = num * num
print("Square:", square)
'''
def get_input():
    """
    Prompt the user to enter a number and return it as an integer.

    Returns:
    int: The number entered by the user.
    """
    return int(input("Enter number: "))
def process_input(num):
    """
    Calculate the square of the given number.

    Parameters:
    num (int): The number to be squared.

    Returns:
    int: The square of the input number.
    """
    return num * num
def output_result(square):
    """
    Print the square of the number.

    Parameters:
    square (int): The square of the number to be printed.
    """
    print("Square:", square)
# Main function to orchestrate the input, processing, and output
def main():
    num = get_input()  # Get user input
    square = process_input(num)  # Process the input to calculate the square
    output_result(square)  # Output the result
if __name__ == "__main__":
    main()  # Run the main function
    