import pytest
from lib.check_todo import *

# Given a the string #TODO only.
# The code will return True
# check_todo("#TODO") => True
def test_single_todo_return_true():
    result = check_todo("#TODO")
    assert result == True

# Given a string that includes lowercase #todo.
# The code will return False
# check_todo("#todo") => False
def test_single_lower_todo_return_false():
    result = check_todo("#todo")
    assert result == False

# Given a sentence including #TODO at the start.
# The code will return True
# check_todo("#TODO remember to do the laundry") => True
def test_string_starting_with_todo():
    result = check_todo("#TODO remember to do the laundry")
    assert result == True

# Given a sentence including #TODO in the middle.
# The code will return True
# check_todo("Go shopping #TODO buy bread") => True
def test_string_middle_with_todo():
    result = check_todo("Go shopping #TODO buy bread")
    assert result == True

# Given an empty string
# The code will return an exception
# check_todo("") => return an exception "No string to check"
def test_an_empty_string():
    with pytest.raises(Exception) as e:
        check_todo("")
    error_message = str(e.value)
    assert error_message == "No string to check"