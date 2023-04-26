#A function called count_words that takes a string as an argument and returns the number of words in that string.
from lib.count_words import *

#This tests an empty string
def test_empty_string_returns_string():
    result = count_words("")
    assert result == ""

#This tests the length of the string.
def test_length_of_string_returns_length():
    result = count_words("This is a string")
    assert result == 4

#This tests if its not a string and returns the item.
def test_if_not_string_return_item():
    result = count_words(66)
    assert result == 66