class TaskTracker():
    def __init__(self):
        self.tasks = [] #An empty list that we can store our todo tasks
    
    def add_todo(self, task):
        if task == " ":
            raise Exception("No task added.")
        self.tasks.append(task) #This will append the list
    
    def view_todo(self):
        return self.tasks #This will return whats in the list
    
    def mark_complete(self, task):
        if task in self.tasks:
            self.tasks.remove(task) #This will remove the task from my list
        else:
            raise Exception("Task not in list, would you like me to add this?")