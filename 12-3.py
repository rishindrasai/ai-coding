#generate a code to sort student records(name,roll no,CGPA) CGPA wise in descending order for placement drive using merge sort and quick sort 
# and compare the time taken by both sorting algorithms. compare the performance for large datasets.display top 10 students
'''import time
import random
class Student:
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa
def merge_sort(students):
    if len(students) > 1:
        mid = len(students) // 2
        left_half = students[:mid]
        right_half = students[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].cgpa > right_half[j].cgpa:
                students[k] = left_half[i]
                i += 1
            else:
                students[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            students[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            students[k] = right_half[j]
            j += 1
            k += 1
def quick_sort(students):
    if len(students) <= 1:
        return students
    else:
        pivot = students[0]
        left = [x for x in students[1:] if x.cgpa > pivot.cgpa]
        right = [x for x in students[1:] if x.cgpa <= pivot.cgpa]
        return quick_sort(left) + [pivot] + quick_sort(right)
# Generate random student records
def generate_students(num_students):
    students = []
    for i in range(num_students):
        name = f"Student_{i+1}"
        roll_no = i + 1
        cgpa = round(random.uniform(0, 10), 2)
        students.append(Student(name, roll_no, cgpa))
    return students
# Compare sorting algorithms
num_students = 10000
students = generate_students(num_students)
students_copy = students.copy()
start_time = time.time()
merge_sort(students)
merge_sort_time = time.time() - start_time
start_time = time.time()
sorted_students = quick_sort(students_copy)
quick_sort_time = time.time() - start_time
print(f"Merge Sort Time: {merge_sort_time:.4f} seconds")
print(f"Quick Sort Time: {quick_sort_time:.4f} seconds")
# Display top 10 students
print("Top 10 Students (Merge Sort):")
for student in students[:10]:
    print(f"Name: {student.name}, Roll No: {student.roll_no}, CGPA: {student.cgpa}")

print("\nTop 10 Students (Quick Sort):")
for student in sorted_students[:10]:
    print(f"Name: {student.name}, Roll No: {student.roll_no}, CGPA: {student.cgpa}")'''

#generate a code to implement bubble sort with ai comments and provide time complexity analysis
def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Time complexity analysis:
# The time complexity of bubble sort is O(n^2) in the worst and average cases
# because it requires two nested loops to compare each element with every other element.
# In the best case, when the array is already sorted, the time complexity is O(n)
# because it only requires one pass to check if the array is sorted.
# Assert test cases
assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert bubble_sort([]) == []
