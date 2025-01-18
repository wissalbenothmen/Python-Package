# test_string_ops.py
from package_creation_tutorial.string_ops import reverse_string, count_vowels, capitalize_words

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_count_vowels():
    assert count_vowels("hello") == 2

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"