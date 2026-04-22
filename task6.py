'''
Refactor inefficient linear searches using appropriate data structures.
• Focus Areas:
o Time complexity
o Data structure choice
Legacy Code:
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
   if u == name:
       found = True
print("Access Granted" if found else "Access Denied")
'''
def check_user_access(users, name):
    """
    Check if the given username exists in the users list.

    Parameters:
    users (list): A list of usernames.
    name (str): The username to check for access.

    Returns:
    str: "Access Granted" if the user is found, otherwise "Access Denied".
    """
    # Convert the list of users to a set for O(1) average time complexity lookups
    user_set = set(users)
    
    if name in user_set:
        return "Access Granted"
    else:
        return "Access Denied"
# Example usage
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
result = check_user_access(users, name)
print(result)
