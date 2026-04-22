
'''Count vowels and consonants in string.
Normal: "hello" → (2,3)
Edge: "" → (0,0)
Only vowels: "aeiou" → (5,0)
Large: Long text
'''
def count_vowels_consonants(s):
    """
    Count the number of vowels and consonants in a given string.

    Parameters:
    s (str): The input string to analyze.

    Returns:
    tuple: A tuple containing the count of vowels and consonants (vowels_count, consonants_count).
    """
    vowels = 'aeiouAEIOU'
    vowels_count = sum(1 for char in s if char in vowels)
    consonants_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    
    return vowels_count, consonants_count
# Example usage
input_string = "hello"
vowels_count, consonants_count = count_vowels_consonants(input_string)
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")  # Output: Vowels: 2, Consonants: 3
input_string = ""
vowels_count, consonants_count = count_vowels_consonants(input_string)
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")  # Output: Vowels: 0, Consonants: 0
input_string = "aeiou"
vowels_count, consonants_count = count_vowels_consonants(input_string)
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")  # Output: Vowels: 5, Consonants: 0
input_string = "This is a long text to test the function with a larger input."
vowels_count, consonants_count = count_vowels_consonants(input_string)
print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")  # Output will vary based on the input string.
    