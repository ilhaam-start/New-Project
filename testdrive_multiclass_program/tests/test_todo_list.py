import pytest
from lib.todo_list import *

"""
Initially this has an empty list of entries
"""
def test_starts_with_empty_list():
    todolist = TodoList()
    assert todolist.all() == []

"""
incomplete raises an error if no todos are added
"""
def test_no_todos_added_raises_exception():
    todolist = TodoList()
    with pytest.raises(Exception) as e:
        todolist.incomplete()
    error_message = str(e.value)
    assert error_message == "No todos in the list."

"""
give up raises an error if no todos are in the list
"""
def test_no_todos_added_raises_exception_for_give_up():
    todolist = TodoList()
    with pytest.raises(Exception) as e:
        todolist.incomplete()
    error_message = str(e.value)
    assert error_message == "No todos in the list."