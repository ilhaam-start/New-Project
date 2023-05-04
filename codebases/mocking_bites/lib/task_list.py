class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        # appends task to list
        self.tasks.append(task)

    def all(self):
        # returns the task list
        return self.tasks
    
    def all_complete(self):
        # if our list is empty return False
        if len(self.tasks) == 0:
            return False
        return all([task.is_complete() for task in self.tasks])
