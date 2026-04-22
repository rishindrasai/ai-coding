'''
Refactor the given poorly structured Python script into a clean, modular, and reusable implementation.
The current program reads a year from the user and prints the corresponding Chinese Zodiac sign. However, the implementation contains repetitive conditional logic, lacks modular design, and does not follow clean coding principles.
Your task is to refactor the code to improve readability, maintainability, and structure.
Chinese Zodiac Cycle (Repeats Every 12 Years)
1. Rat
2. Ox
3. Tiger
4. Rabbit
5. Dragon
6. Snake
7. Horse
8. Goat (Sheep)
9. Monkey
10. Rooster
11. Dog
12. Pig
# Chinese Zodiac Program (Unstructured Version)
# This code needs refactoring.
 
year = int(input("Enter a year: "))
 
if year % 12 == 0:
   print("Monkey")
elif year % 12 == 1:
   print("Rooster")
elif year % 12 == 2:
   print("Dog")
elif year % 12 == 3:
   print("Pig")
elif year % 12 == 4:
   print("Rat")
elif year % 12 == 5:
   print("Ox")
elif year % 12 == 6:
   print("Tiger")
elif year % 12 == 7:
   print("Rabbit")
elif year % 12 == 8:
   print("Dragon")
elif year % 12 == 9:
   print("Snake")
elif year % 12 == 10:
   print("Horse")
elif year % 12 == 11:
   print("Goat")
'''
def get_chinese_zodiac(year):
    """
    Get the Chinese Zodiac sign for a given year.

    Parameters:
    year (int): The year for which to determine the Chinese Zodiac sign.

    Returns:
    str: The Chinese Zodiac sign corresponding to the given year.
    """
    zodiac_signs = [
        "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
        "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
    ]
    
    return zodiac_signs[year % 12]
# Example usage
year = int(input("Enter a year: "))
zodiac_sign = get_chinese_zodiac(year)
print(f"The Chinese Zodiac sign for the year {year} is: {zodiac_sign}") 

