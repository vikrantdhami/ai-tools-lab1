def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    A palindrome reads the same forwards and backwards.
    Ignores spaces and capitalization for accurate checking.
    """
    # Remove spaces and convert to lowercase
    cleaned_string = s.replace(" ", "").lower()
    # Compare the string with its reverse (using slicing [::-1])
    return cleaned_string == cleaned_string[::-1]

def count_words(text):
    """
    Counts the number of words in a given text string.
    Words are considered to be separated by whitespace.
    """
    # .split() breaks the string into a list of words based on spaces
    words_list = text.split()
    # len() counts how many items are in that list
    return len(words_list)

def celsius_to_fahrenheit(c):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Standard formula: F = (C * 9/5) + 32
    """
    return (c * 9 / 5) + 32

# --- Testing the functions ---
if __name__ == "__main__":
    print("--- Testing is_palindrome ---")
    print("racecar ->", is_palindrome("racecar"))
    print("A man a plan a canal Panama ->", is_palindrome("A man a plan a canal Panama"))
    print("hello ->", is_palindrome("hello"))
    
    print("\n--- Testing count_words ---")
    print("'Hello AI Tools Lab!' has", count_words("Hello AI Tools Lab!"), "words.")
    
    print("\n--- Testing celsius_to_fahrenheit ---")
    print("0 degrees C =", celsius_to_fahrenheit(0), "degrees F")
    print("100 degrees C =", celsius_to_fahrenheit(100), "degrees F")