'''Refactor into is_prime(n) and is_twin_prime(p1, p2).
• Add docstrings and optimize.
• Generate a list of twin primes in a given range using AI.
Bad Code Version:
# twin primes bad version
a=11
b=13
fa=0
for i in range(2,a):
if a%i==0:
 fa=1
fb=0
for i in range(2,b):
if b%i==0:
 fb=1
if fa==0 and fb==0 and abs(a-b)==2:
print("Twin Primes")
else:
print("Not Twin Primes")'''
def is_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_twin_prime(p1, p2):
    """Check if two numbers are twin primes."""
    return is_prime(p1) and is_prime(p2) and abs(p1 - p2) == 2
def generate_twin_primes(start, end):   
    """
    Generate a list of twin primes within a given range.

    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    list: A list of tuples, each containing a pair of twin primes.
    """
    twin_primes = []
    for num in range(start, end - 1):
        if is_twin_prime(num, num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes
# Example usage
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False
print(is_twin_prime(11, 13))  # Output: True
print(is_twin_prime(17, 19))  # Output: True
print(is_twin_prime(14, 16))  # Output: False
print(generate_twin_primes(1, 100))  # Output: [(3, 5), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
