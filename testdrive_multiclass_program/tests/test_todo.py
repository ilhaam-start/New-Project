from lib.todo import *

"""
When I initialise a task I get this back
"""
def test_initialise_task_get_it_back():
    todo = Todo("House chores")
    assert todo.task == "House chores"

"""
When I initialise a task return False
"""
def test_mark_complete_return_false():
    todo = Todo("House chores")
    assert todo.complete == False

"""
When I initialise a task and mark complete return True
"""
def test_mark_complete_return_true():
    todo = Todo("House chores")
    todo.mark_complete()
    assert todo.complete == True