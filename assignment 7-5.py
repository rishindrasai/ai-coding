"""def add_item(item, items=None):
	if items is None:
		items = []
	items.append(item)
	return items

print(add_item(1))
print(add_item(2))



#task2
import math

def check_sum():
	return math.isclose(0.1 + 0.2, 0.3)

print(check_sum())

#task 3
def countdown(n):
	if n < 0:
		return
	print(n)
	return countdown(n-1)

countdown(5)

#task 4
def get_value():
	data = {"a": 1, "b": 2}
	return data.get("c", None)

print(get_value())

#task 5
def loop_example():
	i = 0
	while i < 5:
		print(i)
		i += 1

loop_example()

#task 6
a, b, c = (1, 2, 3)
print(a, b, c)

#task 7
def func():
	x = 5
	y = 10
	return x+y

print(func())

#task 8
import math
print(math.sqrt(16))

#task 9
def total(numbers):
    sum_total = 0
    for n in numbers:
        sum_total += n
    return sum_total

print(total([1, 2, 3]))  # Output: 6

#task 10
def calculate_area(length, width):
	return length * width

# Test case 1
print(calculate_area(5, 10))  # Output: 50

# Test case 2
print(calculate_area(3, 7))  # Output: 21

# Test case 3
print(calculate_area(4, 4))  # Output: 16
 
#task 11
def add_values():
	return 5 + int("10")

# Test case 1
print(add_values())  # Output: 15

# Test case 2
print(5 + int("20"))  # Output: 25

# Test case 3
print(10 + int("5"))  # Output: 15

#task 12

def combine():
	return "Numbers: " + str([1, 2, 3])

# Test case 1
print(combine())  # Output: Numbers: [1, 2, 3]

# Test case 2
print("Numbers: " + str([4, 5, 6]))  # Output: Numbers: [4, 5, 6]

# Test case 3
print("Numbers: " + str([7, 8, 9]))  # Output: Numbers: [7, 8, 9]"""

#task 13
def repeat_text():
	return "Hello" * int(2.5)

# Test case 1
print(repeat_text())  # Output: HelloHello

# Test case 2
print("Hi" * int(3.7))  # Output: HiHiHi

# Test case 3
print("Python" * int(1.9))  # Output: Python


 










