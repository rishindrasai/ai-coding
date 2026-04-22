'''
Refactor into a clean reusable function (generate_fibonacci).
• Add docstrings and test cases.
• Compare AI-refactored vs original.
Bad Code Version:
# fibonacci bad version
n=int(input("Enter limit: "))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
c=a+b
print(c)
a=b
b=c
'''
def generate_fibonacci(n):
    """
    Generate a list of Fibonacci numbers up to the nth number.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the Fibonacci sequence up to the nth number.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence
# Test cases
print(generate_fibonacci(0))  # Output: []
print(generate_fibonacci(1))  # Output: [0]
print(generate_fibonacci(2))  # Output: [0, 1]
print(generate_fibonacci(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]   
