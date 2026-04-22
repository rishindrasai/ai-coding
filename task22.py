'''
Refactor code that modifies shared mutable state.
• Focus Areas:
o Functional-style refactoring
o Predictability
Legacy Code:
data = []
def add_item(x):
data.append(x)
add_item(10)
add_item(20)
print(data)
'''
def add_item(data, x):
    """
    Add an item to the data list.

    Parameters:
    data (list): The list to which the item will be added.
    x: The item to be added to the list.

    Returns:
    list: A new list with the item added.
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list.")
    
    new_data = data.copy()  # Create a copy of the original list to avoid modifying it
    new_data.append(x)  # Add the new item to the copied list
    return new_data  # Return the new list with the item added
# Example usage
data = []
data = add_item(data, 10)
data = add_item(data, 20)
print(data)  # Output: [10, 20] 
