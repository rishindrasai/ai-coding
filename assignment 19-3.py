#Create a Python class named Student with appropriate attributes and methods
'''class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_grade(self, grade):
        self.grade = grade


    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"
# convert the above code into equivalent C++ code while properly implementing constructors, suitable data types, and correct access specifiers (private and public)
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int age;
    char grade;

public:
    Student(string name, int age, char grade) {
        this->name = name;
        this->age = age;
        this->grade = grade;
    }

    string getName() {
        return name;
    }

    int getAge() {
        return age;
    }

    char getGrade() {
        return grade;
    }

    void setName(string name) {
        this->name = name;
    }

    void setAge(int age) {
        this->age = age;
    }

    void setGrade(char grade) {
        this->grade = grade;
    }

    void display() {
        cout << "Student(name=" << name << ", age=" << age << ", grade=" << grade << ")" << endl;
    }
};

'''


#Create a Java class checks whether a number is prime with method isPrime() 
'''public class PrimeChecker {
    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[] testNumbers = {29, 15, 17, 20, 23};
        for (int num : testNumbers) {
            if (isPrime(num)) {
                System.out.println(num + " is a prime number.");
            } else {
                System.out.println(num + " is not a prime number.");
            }
        }
    }
}

#convert the above code with isPrime() method into Python code and Test the function with multiple inputs
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function with multiple inputs
test_numbers = [29, 15, 17, 20, 23]
for num in test_numbers:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
'''


#write a pseudocode for sorting numbers (e.g.bubble sort or selection sort)and convert it into executable Python code
'''# Pseudocode for Bubble Sort:
# function bubbleSort(arr):
#     n = length of arr
#     for i from 0 to n-1:
#         for j from 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                 swap arr[j] and arr[j+1]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Test the function with sample input lists
sample_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(sample_list)
print("Sorted list is:", sorted_list)
'''

#write a SQL query (e.g., SELECT name, salary FROM employees WHERE salary > 50000)and generate equivalent Pandas code and also Test the generated code on a sample DataFrame.
'''
import pandas as pd
# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'salary': [60000, 45000, 70000, 30000]
}
df = pd.DataFrame(data)
# SQL Query: SELECT name, salary FROM employees WHERE salary > 50000
filtered_df = df[df['salary'] > 50000][['name', 'salary']]
print(filtered_df)

'''


#write a Python searching algorithm and convert into C and 
# Java sorting program into JavaScript translate a selected algorithm between two programming languages
#Execute and test both versions, Document translation challenges such as(Syntax differences,Library support,Memory management)
# Python searching algorithm (Linear Search)

'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Test the function with a sample input list and target value
sample_list = [5, 3, 2, 8, 1]
target_value = 2
result = linear_search(sample_list, target_value)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")

# C version of Linear Search
#include <stdio.h>
int linear_search(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}
int main() {
    int sample_list[] = {5, 3, 2, 8, 1};
    int target_value = 2;
    int size = sizeof(sample_list) / sizeof(sample_list[0]);
    int result = linear_search(sample_list, size, target_value);
    if (result != -1) {
        printf("Element found at index: %d\n", result);
    } else {
        printf("Element not found in the list.\n");
    }
    return 0;
}

'''
#java and JavaScript sorting program (Selection Sort)
'''// Java version of Selection Sort
public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            int min_idx = i;
            for (int j = i+1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
    public static void main(String[] args) {
        int[] sample_list = {64, 25, 12, 22, 11};
        selectionSort(sample_list);
        System.out.println("Sorted array: ");
        for (int num : sample_list) {
            System.out.print(num + " ");
        }
    }
}
// JavaScript version of Selection Sort
function selectionSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let min_idx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        [arr[i], arr[min_idx]] = [arr[min_idx], arr[i]];
    }
    return arr;
}
// Test the function with a sample input list
let sample_list = [64, 25, 12, 22, 11];
let sorted_list = selectionSort(sample_list);
console.log("Sorted array: ", sorted_list);





''
'''