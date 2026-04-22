"""Task 1#develop a student information management module class should include attributes such as name,roll number and branch and a method display_details() to print student information student examples 5 are enough
class Student:
    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch

    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Branch: {self.branch}")     
# Creating 5 student examples
student1 = Student("Alice", "101", "Computer Science")
student2 = Student("Bob", "102", "Mechanical Engineering")
student3 = Student("Charlie", "103", "Electrical Engineering")
student4 = Student("David", "104", "Civil Engineering")
student5 = Student("Eve", "105", "Chemical Engineering")    
# Displaying student details
student1.display_details()
student2.display_details()
student3.display_details()
student4.display_details()
student5.display_details()

# Task 2: Utility function to display multiples of a given number

def display_multiples_for(num, count=10):
    
    print(f"\nMultiples of {num} using FOR loop:")
    for i in range(1, count + 1):
        print(f"{num} × {i} = {num * i}"
    print()

def display_multiples_while(num, count=10):
  
    print(f"\nMultiples of {num} using WHILE loop:")
    i = 1
    while i <= count:
        print(f"{num} × {i} = {num * i}")
        i += 1
    print()

# Test with examples
display_multiples_for(5)
display_multiples_while(5)

display_multiples_for(7)
display_multiples_while(7)

# Comparison Analysis
print("\n--- LOOP COMPARISON ---")
print("FOR Loop: Best for known iterations, cleaner syntax, automatic counter management")
print("WHILE Loop: Best for conditional iterations, more control, requires manual counter increment")
print("Both produce identical output but differ in readability and use cases")

#task 4
# Task 4: Sum of first n natural numbers

def sum_to_n_for(n):

    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_while(n):
    
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_formula(n):
    
    return n * (n + 1) // 2

# Test examples
print("\n--- SUM OF FIRST N NATURAL NUMBERS ---")
print(f"Sum of first 10 numbers (FOR): {sum_to_n_for(10)}")
print(f"Sum of first 10 numbers (WHILE): {sum_to_n_while(10)}")
print(f"Sum of first 10 numbers (FORMULA): {sum_to_n_formula(10)}")

print(f"\nSum of first 100 numbers (FOR): {sum_to_n_for(100)}")
print(f"Sum of first 100 numbers (WHILE): {sum_to_n_while(100)}")
print(f"Sum of first 100 numbers (FORMULA): {sum_to_n_formula(100)}")

# Analysis
print("\n--- IMPLEMENTATION ANALYSIS ---")
print("FOR Loop: O(n) time complexity, iterative approach")
print("WHILE Loop: O(n) time complexity, more manual control")
print("Mathematical Formula: O(1) time complexity, most efficient for large numbers")"""

# Task 5: Bank Account Management System

class BankAccount:
    """
    A class to manage bank account operations.
    Attributes:
        account_holder (str): Name of the account holder
        account_number (str): Unique account identifier
        balance (float): Current account balance
    """
    
    def __init__(self, account_holder, account_number, initial_balance=0):
        """
        Initialize a bank account with holder details and initial balance.
        
        Args:
            account_holder (str): Name of the account holder
            account_number (str): Unique account number
            initial_balance (float): Starting balance (default: 0)
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        """
        Add money to the account.
        
        Args:
            amount (float): Amount to deposit (must be positive)
        
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return False
        
        self.balance += amount
        print(f"✓ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """
        Remove money from the account with sufficient balance check.
        
        Args:
            amount (float): Amount to withdraw (must be positive and available)
        
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient balance! Available: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        print(f"✓ Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def check_balance(self):
        """
        Display the current account balance.
        
        Returns:
            float: Current balance
        """
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")
        return self.balance


# Test examples
print("\n--- BANK ACCOUNT MANAGEMENT SYSTEM ---\n")

account1 = BankAccount("John Doe", "ACC001", 5000)
account2 = BankAccount("Jane Smith", "ACC002", 3000)

# Operations for Account 1
account1.check_balance()
account1.deposit(1500)
account1.withdraw(2000)
account1.withdraw(10000)  # Insufficient balance
account1.check_balance()

print()

# Operations for Account 2
account2.check_balance()
account2.deposit(2500)
account2.withdraw(1000)
account2.check_balance()

# Analysis
print("\n--- CLASS STRUCTURE ANALYSIS ---")
print("Attributes: account_holder, account_number, balance")
print("Methods: __init__(), deposit(), withdraw(), check_balance()")
print("Key Features:")
print("  • Balance validation before withdrawal")
print("  • Error handling for invalid amounts")
print("  • Return values for transaction status")
print("  • Clear user feedback with formatted output")