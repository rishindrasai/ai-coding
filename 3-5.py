'''def is_leap_year(year: int) -> bool:
    """
    Return True if 'year' is a leap year, otherwise False.

    Rules:
    - A year is a leap year if it is divisible by 4,
      EXCEPT years divisible by 100 are NOT leap years,
      UNLESS they are also divisible by 400.
    """
    if year % 400 == 0:
        return True      # divisible by 400 → leap year
    if year % 100 == 0:
        return False     # divisible by 100 but not 400 → not a leap year
    if year % 4 == 0:
        return True      # divisible by 4 but not by 100 → leap year
    return False         # all other years → not a leap year
print(1900, is_leap_year(1900))  # Expected: False  (divisible by 100, not by 400)
print(2000, is_leap_year(2000))  # Expected: True   (divisible by 400)
print(2024, is_leap_year(2024))  # Expected: True   (divisible by 4, not by 100)'''


'''

def gcd(a: int, b: int) -> int:
    """
    Return the Greatest Common Divisor of two integers using the Euclidean algorithm.
    Returns a non-negative result regardless of input signs.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))      # Expected: 6
print(gcd(100, 50))     # Expected: 50
print(gcd(-12, 8))      # Expected: 4
print(gcd(17, 19))      # Expected: 1'''


'''
def gcd(a: int, b: int) -> int:
    """
    Return the Greatest Common Divisor of two integers using
    the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """
    Return the Least Common Multiple of two integers using the relationship:
    LCM(a, b) = |a * b| // GCD(a, b)
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(abs(a), abs(b))

print(lcm(12, 18))      # Expected: 36
print(lcm(100, 50))     # Expected: 100
print(lcm(-12, 8))      # Expected: 24
print(lcm(17, 19))      # Expected: 323'''


