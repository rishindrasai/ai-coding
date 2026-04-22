
'''eliminate unnecessary global variables from the
code.
Identify global variables used across functions.
Refactor the code to pass values using function parameters.
Improve modularity and testability.'''

'''rate = 0.1
def calculate_interest(amount): 
    return amount * rate
print(calculate_interest(1000))'''
def calculate_interest(amount, rate):
    return amount * rate
# Example usage
amount = 1000
rate = 0.1
print(calculate_interest(amount, rate))
    