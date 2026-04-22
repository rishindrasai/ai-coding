'''def reverse_string(s):'''
"""   Reverse a string.
    
    Args:
        s (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """""""
    return s[::-1]"""



'''def check_strength(password):
        """
        Check the strength of a password.
        
        Args:
            password (str): The password to check.
        
        Returns:
            str: The strength level ('Weak', 'Medium', or 'Strong').
        
        Example:
            >>> check_strength("Pass123!")
            'Strong'
        """
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        criteria_met = sum([has_upper, has_lower, has_digit, has_special])
        
        if len(password) < 8 or criteria_met < 2:
            return "Weak"
        elif criteria_met == 2 or len(password) < 12:
            return "Medium"
        else:
            return "Strong"'''
'''def square(n):
                """
                Calculate the square of a number.
                
                Args:
                    n (int or float): The number to square.
                
                Returns:
                    int or float: The square of the number.
                
                Example:
                    >>> square(5)
                    25
                """
                return n * n


def cube(n):
                """
                Calculate the cube of a number.
                
                Args:
                    n (int or float): The number to cube.
                
                Returns:
                    int or float: The cube of the number.
                
                Example:
                    >>> cube(3)
                    27
                """
                return n * n * n


def factorial(n):
                """
                Calculate the factorial of a number.
                
                Args:
                    n (int): A non-negative integer.
                
                Returns:
                    int: The factorial of n.
                
                Raises:
                    ValueError: If n is negative.
                
                Example:
                    >>> factorial(5)
                    120
                """
                if n < 0:
                    raise ValueError("Factorial is not defined for negative numbers")
                if n == 0 or n == 1:
                    return 1
                result = 1
                for i in range(2, n + 1):
                    result *= i
                return result

def mark_present(student):
                    """
                    Mark a student as present.
                    
                    Args:
                        student (str): The name of the student.
                    
                    Returns:
                        str: Confirmation message.
                    
                    Example:
                        >>> mark_present("John")
                        'John marked present'
                    """
                    return f"{student} marked present"


def mark_absent(student):
                    """
                    Mark a student as absent.
                    
                    Args:
                        student (str): The name of the student.
                    
                    Returns:
                        str: Confirmation message.
                    
                    Example:
                        >>> mark_absent("John")
                        'John marked absent'
                    """
                    return f"{student} marked absent"


def get_attendance(student):
                    """
                    Get the attendance status of a student.
                    
                    Args:
                        student (str): The name of the student.
                    
                    Returns:
                        str: The attendance status of the student.
                    
                    Example:
                        >>> get_attendance("John")
                        'John attendance record'
                    """
                    return f"{student} attendance record'''












