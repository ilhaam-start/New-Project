import pytest
from lib.checking_grammar import *

#This tests empty string
def test_checking_empty_string():
    with pytest.raises(Exception) as e:
        checking_grammar("")
    error_message = str(e.value)
    assert error_message == "No text to check."

# Given a text of words that start with uppercase and ends with '.'
# The code will return True
# checking_grammar("Hello, python.") => True
def test_checking_grammar():
    grammar = checking_grammar("Hello, python.")
    assert grammar == True

# Given a text of words that start with uppercase and ends with '?'
# The code will return True
# checking_grammar("What is the date?") => True
def test_checking_uppercase_with_question_mark():
    grammar = checking_grammar("What is the date?")
    assert grammar == True

# Given a text of words that start with uppercase and doesn't end with '.'
# The code will return False
# checking_grammar("Hello, python") => False
def test_checking_uppercase_no_punct():
    grammar = checking_grammar("Hello, python")
    assert grammar == False

# Given a text of words that start with lowercase and ends with '.'
# The code will return False
# checking_grammar("hello, python.") => False
def test_checking_lowercase_punct():
    grammar = checking_grammar("hello, python.")
    assert grammar == False

# Given a text of words that start with lowercase and doesn't end with '.'
# The code will return False
# checking_grammar("hello, python") => False
def test_checking_no_lowercase_no_punct():
    grammar = checking_grammar("hello, python")
    assert grammar == False