# Challenge Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string #TODO.

## Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._


def check_todo(text):
    # This checks if a text include the string #TODO
    # Parameters: (list all parameters and their types)
        text: a string representing text
    # Returns: (state the return value and its type)
        a boolean (True, False)
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

## Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a the string #TODO only.
The code will return True
"""
check_todo("#TODO") => True

"""
Given a string that includes lowercase #todo.
The code will return False
"""
check_todo("#todo") => False

"""
Given a sentence including #TODO at the start.
The code will return True
"""
check_todo("#TODO remember to do the laundry") => True

"""
Given a sentence including #TODO at the end.
The code will return True
"""
check_todo("Go shopping #TODO buy bread") => True

"""
Given an empty string
The code will return an exception
"""
check_todo("") => return an exception "No string to check"




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