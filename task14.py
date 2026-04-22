
''' Generate Lucas sequence up to n terms.(Starts with 2,1, then Fn = Fn-1 + Fn-2)
Normal: 5 → [2, 1, 3, 4, 7]
Edge: 1 → [2]
Negative: -5 → Error
Large: 10 (last element = 76).
'''
def lucas_sequence(n):
    """
    Generate the Lucas sequence up to n terms.

    Parameters:
    n (int): The number of terms in the Lucas sequence to generate.

    Returns:
    list: A list containing the Lucas sequence up to n terms.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    sequence = []
    a, b = 2, 1  # Starting values for the Lucas sequence
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # Update to the next two terms in the sequence
    return sequence
# Example usage
print(lucas_sequence(5))  # Output: [2, 1,3, 4, 7]
print(lucas_sequence(1))  # Output: [2]
try:
    print(lucas_sequence(-5))  # Should raise ValueError
except ValueError as e:
    print(e)  # Output: Input must be a positive integer.
print(lucas_sequence(10))  # Output: [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]            
