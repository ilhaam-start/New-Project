# Grammar Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._


def checking_grammar(text):
    # This checks that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
    # Parameters: (list all parameters and their types)
        text: a string representing text
    # Returns: (state the return value and its type)
        a boolean (True, False)
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

## Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a text of words that start with uppercase and ends with '.'
The code will return True
"""
checking_grammar("Hello, python.") => True

"""
Given a text of words that start with uppercase and doesn't end with '.'
The code will return False
"""
checking_grammar("Hello, python") => False

"""
Given a text of words that start with lowercase and ends with '.'
The code will return False
"""
checking_grammar("hello, python.") => False

"""
Given a text of words that start with lowercase and doesn't end with '.'
The code will return False
"""
checking_grammar("hello, python") => False


## 4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
Ensure all test function names are unique, otherwise pytest will ignore them!