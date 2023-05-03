from lib.todo_list import *
from lib.todo import *

"""
First, when I add multiple tasks to my todo's it returns this in a list
"""
def test_add_multiple_tasks_returned_in_list():
    todolist = TodoList()
    task_1 = Todo("Book Doctors Appointment")
    task_2 = Todo("Go grocery shopping")
    task_3 = Todo("Meet friends for lunch")
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    assert todolist.all() == [task_1, task_2, task_3]

"""
If I add two tasks that are incomplete, and call the incomplete
method, this will return a list of the incomplete tasks.
"""
def test_add_tasks_return_incomplete_list():
    todolist = TodoList()
    task_1 = Todo("Book Doctors Appointment")
    task_2 = Todo("Go grocery shopping")
    todolist.add(task_1)
    todolist.add(task_2)
    assert todolist.incomplete() == [task_1, task_2]

"""
If I add two tasks and one is incomplete, and call the incomplete
method, this will return a list of the single incomplete tasks.
"""
def test_add_two_tasks_return_one_incomplete():
    todolist = TodoList()
    task_1 = Todo("Book Doctors Appointment")
    task_2 = Todo("Go grocery shopping")
    todolist.add(task_1)
    todolist.add(task_2)
    task_1.mark_complete()
    assert todolist.incomplete() == [task_2]

"""
If I add three tasks and all are incomplete, and call the incomplete
method, this will return a list of the all incomplete tasks.
"""
def test_add_three_tasks_return_full_incomplete_list():
    todolist = TodoList()
    task_1 = Todo("Book Doctors Appointment")
    task_2 = Todo("Go grocery shopping")
    task_3 = Todo("Meet friends for lunch")
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    assert todolist.incomplete() == [task_1, task_2, task_3]

"""
If I add three tasks and all are complete, and I call the complete
method, this will return a list of the all complete tasks.
"""
def test_add_three_tasks_return_full_complete_list():
    todolist = TodoList()
    task_1 = Todo("Book Doctors Appointment")
    task_2 = Todo("Go grocery shopping")
    task_3 = Todo("Meet friends for lunch")
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    task_1.mark_complete()
    task_2.mark_complete()
    task_3.mark_complete()
    assert todolist.complete() == [task_1, task_2, task_3]

"""
If I add three tasks and 2 are complete, and I call the give-up
method, this will complete the tasks but return nothing
"""
def test_add_three_tasks_give_up_on_list_return_all_true():
    todolist = TodoList()
    task_1 = Todo("Book Doctors Appointment")
    task_2 = Todo("Go grocery shopping")
    task_3 = Todo("Meet friends for lunch")
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    task_1.mark_complete()
    task_2.mark_complete()
    assert todolist.give_up() == None
