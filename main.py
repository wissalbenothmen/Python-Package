# main.py
from package_creation_tutorial.string_ops import reverse_string, count_vowels, capitalize_words
from package_creation_tutorial.string_ops import reverse_string
import os  # Importation inutile
def main():
    test_string = "hello world"
    print(f"Original string: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Vowel count: {count_vowels(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")

if __name__ == "__main__":
    main()