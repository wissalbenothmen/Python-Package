import unittest
from package_creation_tutorial.string_ops import (
    reverse_string, 
    count_vowels, 
    capitalize_words, 
    remove_extra_spaces, 
    is_palindrome, 
    to_snake_case
)

class TestStringOps(unittest.TestCase):
    def test_reverse_string(self):
        """Test the reverse_string function."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_count_vowels(self):
        """Test the count_vowels function."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_capitalize_words(self):
        """Test the capitalize_words function."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")

    def test_remove_extra_spaces(self):
        """Test the remove_extra_spaces function."""
        self.assertEqual(remove_extra_spaces("  hello   world  "), "hello world")
        self.assertEqual(remove_extra_spaces("multiple   spaces   here"), "multiple spaces here")
        self.assertEqual(remove_extra_spaces("\t tabs\t  and\nlines  "), "tabs and lines")

    def test_is_palindrome(self):
        """Test the is_palindrome function."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))  # empty string is considered palindrome

    def test_to_snake_case(self):
        """Test the to_snake_case function."""
        self.assertEqual(to_snake_case("Hello World"), "hello_world")
        self.assertEqual(to_snake_case("camelCaseString"), "camel_case_string")
        self.assertEqual(to_snake_case("simple"), "simple")
        self.assertEqual(to_snake_case("UPPER CASE"), "upper_case")

if __name__ == '__main__':
    unittest.main()