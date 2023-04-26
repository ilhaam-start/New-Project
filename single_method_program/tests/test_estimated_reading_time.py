import pytest
from lib.estimated_reading_time import *

#This tests for 100 words and returns 0.5 minutes
def test_hundred_words_return_point_five():
    result = estimated_reading_time("My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now")
    assert result == 0.5

#This tests for 200 words and returns 1 minute
def test_twohundred_words_return_one():
    result = estimated_reading_time("My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now")
    assert result == 1

#This tests for 400 words and returns 2 minutes
def test_fourhundred_words_return_one():
    result = estimated_reading_time("My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now My name is ilhaam and i am studying python now")
    assert result == 2

#This tests if there is no text in the string and returns an error
def test_empty_string():
    with pytest.raises(Exception) as e:
        estimated_reading_time("")
    error_message = str(e.value)
    assert error_message == "can't estimate reading time for empty text"