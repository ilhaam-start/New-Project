# Reading time Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._


def estimated_reading_time(text):
    # This returns the estimated reading time for a specific text, assuming the reader can read 200 WPM.
    # Parameters: (list all parameters and their types)
        text: a string representing text
    # Returns: (state the return value and its type)
        a float representing reading time
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests

## Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a text of 200 words
The code will return 1 as the reading time
"""
estimated_reading_time(...200words...) => [1.0]

"""
Given a text of 400 words
The code will return 2 as the reading time
"""
estimated_reading_time(...400words...) => [2.0]

"""
Given a text of 100 words
The code will return 0.5 as the reading time
"""
estimated_reading_time(...100words...) => [0.5]

"""
Given a text of no words
The code will return an error
"""
estimated_reading_time("") => [Raises error: can't estimate reading time for empty text]


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