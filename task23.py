'''
simplify and modularize complex validation
rules.
• Focus Areas:
o Readability
o Testability
Legacy Code:
password = input("Enter password: ")
if len(password) >= 8:
if any(c.isdigit() for c in password):
if any(c.isupper() for c in password):
print("Valid Password")
else:
print("Must contain uppercase")
else:
print("Must contain digit")
else:
print("Password too short")
'''
def validate_password(password):
    """
    Validate the password based on specific rules.

    Parameters:
    password (str): The password to validate.

    Returns:
    str: A message indicating whether the password is valid or the reason why it is not.
    """
    if len(password) < 8:
        return "Password too short"
    
    if not any(c.isdigit() for c in password):
        return "Must contain digit"
    
    if not any(c.isupper() for c in password):
        return "Must contain uppercase"
    
    return "Valid Password"
# Example usage
password = input("Enter password: ")    
validation_result = validate_password(password)
print(validation_result)
