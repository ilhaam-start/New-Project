# Use mocking techniques to add some tests that fully test the behaviour of TaskList.
# Unit test `#tasks` and `#all_complete` behaviour

from lib.task_list import *
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def test_adding_a_task_to_our_list():
    task_1 = TaskList()
    task_1.add("go grocery shop")
    assert task_1.all() == ["go grocery shop"]

def test_adding_multiple_tasks_to_our_list():
    tasks = TaskList()
    tasks.add("go grocery shop")
    tasks.add("wash the dishes")
    assert tasks.all() == ["go grocery shop", "wash the dishes"]

def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_tasks_added_to_list():
    tasks_added = TaskList()
    tasks_added.add("babysitting") 
    assert tasks_added.tasks == ["babysitting"]

"""
plan for mocking - the behaviour of our Task_List class
> #all_complete and #is_complete
"""
def test_mocking_all_complete_when_task_is_completed_returns_true():
    task_1 = TaskList()
    task_1_mock = Mock()
    task_1_mock.is_complete.return_value = True
    task_1.add(task_1_mock)
    assert task_1.all_complete() == True
