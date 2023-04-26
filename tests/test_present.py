import pytest

from lib.present import *

#Here we test for when more than one present is wrapped 
def test_present_wrapped_twice():
    present = Present()
    present.wrap("your present") # we need to pass an argument into here first before the exception
    with pytest.raises(Exception) as e:
        present.wrap("another present") #when we try to pass another one then we get the error message below
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped." #error message

# Here we test for when we unwrap a present that isn't wrapped
def test_present_already_unwrapped():
    present = Present()
    present.wrap(None) #we haven't wrapped anything
    with pytest.raises(Exception) as e:
        present.unwrap() #this is where the error will be because there is nothing to unwrap
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

#Here we test if it unwraps correctly
def test_wrap_has_none():
    present = Present()
    present.wrap("candle")
    assert present.unwrap() == "candle"

#Here we test
def test_wrap_different_parameter():
    present = Present()
    present.wrap(22)
    with pytest.raises(Exception) as e:
        present.wrap(33)
    assert present.unwrap() == 22