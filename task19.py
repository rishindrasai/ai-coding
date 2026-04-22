
'''Refactor inefficient linear searches using appropriate
data structures.
Time complexity
Data structure choice'''

users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
    if u == name:
        found = True
print("Access Granted" if found else "Access Denied")
