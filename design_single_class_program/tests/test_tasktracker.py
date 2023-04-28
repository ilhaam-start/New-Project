import pytest
from lib.tasktracker import *

#Given a task
#add_todo adds the task to the todo list
def test_task_added_to_list():
    tasktracker = TaskTracker()
    result = tasktracker.add_todo("Do the laundry")
    assert result == None

#Given multiple tasks
#add_todo adds all the tasks to the todo list
def test_multiple_tasks_added_to_list():
    tasktracker = TaskTracker()
    tasktracker.add_todo("Do the laundry")
    tasktracker.add_todo("Grocery Shopping")
    tasktracker.add_todo("Take notes on GS")
    tasktracker.add_todo("Cook dinner")
    assert tasktracker.view_todo() == ["Do the laundry", "Grocery Shopping", "Take notes on GS", "Cook dinner"]

#Given an empty task
#add_todo raises an exception
def test_an_empty_string():
    tasktracker = TaskTracker()
    with pytest.raises(Exception) as e:
        tasktracker.add_todo(" ")
    error_message = str(e.value)
    assert error_message == "No task added."

#Given that task is completed
#mark_complete removes the task from the list and returns the reduced list
def test_mark_complete_removes_task_return_list():
    tasktracker = TaskTracker()
    tasktracker.add_todo("Do the laundry")
    tasktracker.add_todo("Grocery Shopping")
    tasktracker.add_todo("Take notes on GS")
    tasktracker.mark_complete("Do the laundry")
    result = tasktracker.view_todo() 
    assert result == ["Grocery Shopping", "Take notes on GS"]

#Given that task not in the list is marked completed
#mark_complete will raise an error

def test_completing_task_not_in_list():
    tasktracker = TaskTracker()
    tasktracker.add_todo("Do the laundry")
    tasktracker.add_todo("Grocery Shopping")
    tasktracker.add_todo("Take notes on GS")
    with pytest.raises(Exception) as e:
        tasktracker.mark_complete("Mow the lawn")
    error_message = str(e.value)
    assert error_message == "Task not in list, would you like me to add this?"