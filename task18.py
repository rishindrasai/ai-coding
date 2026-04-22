
'''refactor repeated file open/read/close logic.
DRY principle
Context managers
Function reuse'''

f = open("lab 13.5/data1.txt")
print(f.read())
f.close()
f = open("lab 13.5/data2.txt")
print(f.read())
f.close()
