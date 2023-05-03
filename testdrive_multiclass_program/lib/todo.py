class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        self.task = task #   initialises and sets the task property
        self.complete = False #   initialises and sets the complete property to False

    def mark_complete(self):
        self.complete = True # Sets the complete property to True