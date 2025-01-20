def reverse_string(s: str) -> str:
    """
    Reverse the given string.
    Args:
        s (str): The input string to be reversed.
    Returns:
        str: The reversed string.
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Count the number of vowels in the given string.
    Args:
        s (str): The input string to count vowels from.
    Returns:
        int: The number of vowels in the string.
    """
    vowels: str = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the given string.
    Args:
        s (str): The input string to capitalize.
    Returns:
        str: A new string with each word capitalized.
    """
    return ' '.join(word.capitalize() for word in s.split())

def remove_extra_spaces(s: str) -> str:
    """
    Remove extra whitespace from a string, including leading/trailing spaces
    and multiple spaces between words.
    Args:
        s (str): The input string to clean.
    Returns:
        str: The string with normalized spacing.
    """
    return ' '.join(s.split())

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Ignores case and non-alphanumeric characters.
    Args:
        s (str): The input string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric chars and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def to_snake_case(s: str) -> str:
    """
    Convert a string to snake_case format.
    Args:
        s (str): The input string to convert (can be space-separated or camelCase).
    Returns:
        str: The string in snake_case format.
    """
    # First replace any spaces with underscores
    s = s.replace(' ', '_')
    
    # Handle camelCase by adding underscore before capital letters
    result = s[0].lower()
    for char in s[1:]:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    
    return result.lower()

