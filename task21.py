'''
refactor a performance-heavy loop handling
large data.
• Focus Areas:
o Algorithmic optimization
o Use of built-in functions
Legacy Code:
total = 0
for i in range(1, 1000000):
if i % 2 == 0:
total += i
print(total)
'''
def sum_of_squares(numbers):
    total = 0
    for number in numbers:
        total += number ** 2
    return total
# Refactored code using built-in functions and list comprehension for better performance
def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)
# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_of_squares(numbers))  # Output: 55
