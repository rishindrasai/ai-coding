#task 1
'''def is_valid_email(email: str) -> bool:
    # Condition 1: Email must not start or end with '@' or '.'
    if email.startswith('@') or email.startswith('.') or \
       email.endswith('@') or email.endswith('.'):
        return False

    # Condition 2: Must contain exactly one '@'
    if email.count('@') != 1:
        return False

    # Condition 3: Must contain at least one '.'
    if '.' not in email:
        return False

    # Split local and domain parts
    local_part, domain_part = email.split('@')

    # Condition 4: Local and domain parts must not be empty
    if not local_part or not domain_part:
        return False

    # Condition 5: '.' must exist in domain part
    if '.' not in domain_part:
        return False

    return True
# Test cases
print(is_valid_email("test@example.com"))  # Should return True
print(is_valid_email("test@"))             # Should return False
print(is_valid_email("@example.com"))      # Should return False
print(is_valid_email("test@example"))      # Should return False
print(is_valid_email("test@example..com")) # Should return False
print(is_valid_email("test@.com"))         # Should return False
print(is_valid_email("test@.example.com")) # Should return False
print(is_valid_email("test@example.com.")) # Should return False
print(is_valid_email(""))                  # Should return False
print(is_valid_email("test@@example.com")) # Should return False

#task 2
def assign_grade(score: int) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"

# Test cases
print(assign_grade(59))   # Should return "F"
print(assign_grade(60))   # Should return "D"
print(assign_grade(69))   # Should return "D"
print(assign_grade(70))   # Should return "C"
print(assign_grade(79))   # Should return "C"
print(assign_grade(80))   # Should return "B"
print(assign_grade(89))   # Should return "B"
print(assign_grade(90))   # Should return "A"
print(assign_grade(100))  # Should return "A"
print(assign_grade(101))  # Should return "Invalid score"

#task 3
import string
def is_sentence_palindrome(sentence):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_sentence = ''.join(char for char in sentence if char.isalnum()).lower()
    # Check if the cleaned sentence is equal to its reverse
    return cleaned_sentence == cleaned_sentence[::-1]
# Test cases
print(is_sentence_palindrome("A man a plan a canal Panama"))  # Should return True
print(is_sentence_palindrome("Hello World"))                    # Should return False  
print(is_sentence_palindrome("No 'x' in Nixon"))               # Should return True
print(is_sentence_palindrome("Was it a car or a cat I saw?"))  # Should return True
print(is_sentence_palindrome("This is not a palindrome"))      # Should return False

#task 4

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float):
        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price

    def remove_item(self, name: str):
        if name in self.items:
            del self.items[name]
        else:
            return "Item not found in cart."

    def total_cost(self) -> float:
        return sum(self.items.values())
# Test cases
cart = ShoppingCart()
cart.add_item("Apple", 1.0)
cart.add_item("Banana", 0.5)
print(cart.total_cost())  # Should return 1.5
cart.add_item("Apple", 1.0)
print(cart.total_cost())  # Should return 2.5
cart.remove_item("Banana")
print(cart.total_cost())  # Should return 2.0
cart.remove_item("Orange")  # Should return "Item not found in cart."   
print(cart.total_cost())  # Should return 2.0'''

#task 5
from datetime import datetime
def convert_date_format(date_str: str) -> str:
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."
# Test cases
print(convert_date_format("2024-06-15"))  # Should return "15-06-2024"
print(convert_date_format("2024/06/15"))  # Should return "Invalid date format. Please use 'YYYY-MM-DD'."
print(convert_date_format("15-06-2024"))  # Should return "Invalid date format. Please use 'YYYY-MM-DD'."
print(convert_date_format("2024-13-01"))  # Should return "Invalid date format. Please use 'YYYY-MM-DD'."
print(convert_date_format("2024-06-31"))  # Should return "Invalid date format. Please use 'YYYY-MM-DD'.'''