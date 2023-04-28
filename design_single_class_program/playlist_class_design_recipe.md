1. Describe the Problem

Within the class:


2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

"""
class TaskTracker():
    # User-facing properties:
    #   name: string
    
    def __init__(self, name):
        # Parameters:
        #   name: string representing name
        #   Holds a list that is updated
        pass # No code here yet

    def add_todo(self, task):
        # Parameters:
        #   task: string representing task
        pass # No code here yet

    def view_todo(self):
        # Parameters:
        #   None
        # Returns:
        #   all the tasks in todo that haven't been completed
        pass # No code here yet

    def mark_complete(self, task):
        # Parameters:
        #   task: string representing the tasks.
        # Returns:
        #   Removes the completed task from the list and returns the new list
        pass # No code here yet
"""

3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
Given a task
#add_todo adds the task to the todo list
"""
tasktracker = TaskTracker()
tasktracker.add_todo("Do the laundry")
tasktracker = TaskTracker() # => adds "Do the laundry" to list

"""
Given an empty task
#add_todo raises an exception
"""
tasktracker = TaskTracker()
tasktracker.add_todo("") # raises an error with the message "No task added."

"""
Given that task is completed
#mark_complete still removes the task from the list and returns the reduced list
"""
tasktracker = TaskTracker()
tasktracker.mark_complete("Do the laundry")
tasktracker.view_todo() # => should return the reduced list

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
