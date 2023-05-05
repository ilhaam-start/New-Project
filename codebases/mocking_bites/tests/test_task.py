import pytest
from lib.task import *
from lib.task_formatter import *
from unittest.mock import Mock

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

"""
I can do a mock test for the task-formatter, to check that an unchecked
box is return if the task is not complete
"""
def test_format_returns_unchecked_when_task_not_complete():
    task = Mock()
    task.title = "wash dishes"
    task.is_complete.return_value = False
    formatter = TaskFormatter(task)
    assert formatter.format() == "- [ ] wash dishes"

"""
I can do a mock test for the task-formatter, to check that a checked
box is returned if the task is complete
"""
def test_format_returns_checked_when_task_complete():
    task = Mock()
    task.title = "wash dishes"
    task.is_complete.return_value = True
    formatter = TaskFormatter(task)
    assert formatter.format() == "- [x] wash dishes"

# def test_if_title_is_not_a_string_raise_exception_error():
#     with pytest.raises(Exception) as err:
#         task = Task()
#     assert str(err.value) == "Wrong data type for title"
