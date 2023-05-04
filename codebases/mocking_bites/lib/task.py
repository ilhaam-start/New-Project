class Task:
    def __init__(self, title):
        # if self.title != type(str):
        #     raise Exception("Wrong data type for title")
        self.title = title
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_complete(self):
        return self.complete
    