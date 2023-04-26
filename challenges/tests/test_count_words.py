#A function called count_words that takes a string as an argument and returns the number of words in that string.
from lib.count_words import *

#This tests an empty string
def test_empty_string_returns_string():
    result = count_words("")
    assert result == 0

#This tests the length of the string.
def test_length_of_string_returns_length():
    result = count_words("This is a string")
    assert result == 4

#This tests a string with special characters
def test_string_with_special_characters_returns_length():
    result = count_words("This is @ a string !")
    assert result == 6

#This tests for one long string
def test_a_string_all_together():
    result = count_words("Thisisalongstring")
    assert result == 1