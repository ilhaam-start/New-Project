class TodoList:
    def __init__(self):
        self.todolist = [] #empty list to store the todos

    def add(self, todo):
        self.todolist.append(todo) #this appends the given todo to the list above

    def all(self):
        return self.todolist #this shows us the list

    def incomplete(self):
        if self.todolist == []:
            raise Exception("No todos in the list.")
        return [todo for todo in self.todolist if not todo.complete]
    #This says return the incomplete list if its not in complete

    def complete(self):
        return [todo for todo in self.todolist if todo.complete]
    #This says return the complete list if its in complete

    def give_up(self):
        if self.todolist == []:
            raise Exception("No todos in the list.")
        for todo in self.todolist:
            todo.mark_complete()
        #for each todo in our list this calls mark_complete to complete them