import pytest
from lib.task import *

def test_constructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

def test_task_initialise_to_false_when_called():
    task_false = Task("sweep the floor")
    assert task_false.complete == False

def test_can_be_marked_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.is_complete() == True

# def test_if_title_is_not_a_string_raise_exception_error():
#     with pytest.raises(Exception) as err:
#         task = Task()
#     assert str(err.value) == "Wrong data type for title"
