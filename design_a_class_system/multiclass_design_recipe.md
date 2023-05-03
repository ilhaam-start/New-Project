Multi-Class Planned Design Recipe

1. Describe the Problem

"""
As a user
So that I can record my experiences
I want to keep a regular diary
"""
"""
As a user
So that I can reflect on my experiences
I want to read my past diary entries
"""
"""
As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed
"""
"""
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
"""
* Add todos, mark complete, list complete, incomplete

"""
As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
"""
A phone number starts with zero and is 11 digits long.

# NOUNS
> experiences
> diary
> past diary entries
> day
> time
> reading speed
> tasks
> todo list
> contact list
> mobile numbers

# VERBS 
> add diary entries
> keep diary
> reflect
> read diary entries
> select diary entries to read based on time available and reading speed
> add tasks to todo list
> see a list of mobile numbers in diary entries
> mark complete
> list complete
> list incomplete
> add


2. Design the Class System


Class Diary():

    def add(self, diary_entry):
        #diary_entry: intance of DiaryEntry
        #Returns: Nothing
        #Side-effects: adds to list of diary entries
        pass
    
    def all(self):
        # returns a list of DiaryEntry instances
        pass

Class DiaryEntry():
        
        #public properties:
        #title: string representing title
        #contents: string representing contents

    def __init__(self, title, contents):
        #title: string representing title
        #contents: string representing contents
        #side-effects: sets the above properties
        pass
    

Class TaskList():
    
    def add(self, task):
        #task: an instance of Task
        #returns nothing
        #side-effects: adds to lists of tasks
        pass
    def all_incomplete(self):
    # returns a list of instances of Task representing incomplete tasks.
        pass
    def all_complete(self):
    # returns a list of instances of Task representing complete tasks.
        pass

Class Task():

        #public properties:
        #title: string representing a job to do

    def __init__(self, title):
        #title: string representing a job to do
        #side-effects: sets the above properties
        pass
    
    def mark_complete(self):
        #side effect: marks the task as complete and returns nothing
        pass

Class PhoneNumberExtractor():
    
    def __init__(self, diary):
        #diary: an instance of diary
        #side-effects: sets diary property
        pass
    
    def extract(self):
        #returns a list of strings representing a list of phone numbers
        pass

Class ReadableEntryExtractor():

    def __init__(self, diary):
        #diary: an instance of diary
        #side-effects: sets diary property
        pass
    
    def extract(self, wpm, minutes):
        #wpm: integer
        #minutes: integer
        #returns the longest diary entry that can be read
        in the time given the wpm and minutes
        pass

3. Create Examples as Integration Tests

Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
When I add multiple diary entries, 
#all lists them in the order they were added
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "My contents 1")
entry_2 = DiaryEntry("This Title", "My contents 2")
entry_3 = DiaryEntry("This Title", "My contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() == [entry_1, entry_2, entry_3]

"""
When I add multiple tasks and I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the monkey")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.all_incomplete() == [task_1, task_2, task_3]

"""
When I add multiple tasks and I mark one complete
#all_incomplete lists the incomplete tasks only
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the monkey")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() == [task_1, task_3]

"""
When I add multiple tasks and I mark one complete
#all_complete lists the complete tasks only
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the monkey")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() == [task_2]

"""
When I add multiple diary entries, 
And I call #PhoneNumberExtractor
I get a list of phone numbers from all diary entries
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "My number is 07956247381 and yours is 07956738456")
entry_2 = DiaryEntry("This Title", "My contents 2")
entry_3 = DiaryEntry("This Title", "My new number is 07547823459")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() == ["07956247381", "07956738456", "07547823459"]

"""
When I add a diary entry, 
And I call #PhoneNumberExtractor
it ignores invalid phone numbers
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "My number is 07956247381 and yours is 07956738456, 0794567")
diary.add(entry_1)
extractor = PhoneNumberExtractor(diary)
extractor.extract() == ["07956247381", "07956738456"]

"""
When I add no diary entries
and I call Phone numberExtractor
it returns an empty list []
"""
diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract() == []

"""
When I add multiple diary entries, 
And I call #PhoneNumberExtractor
It ignores duplicate numbers
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "My number is 07956247381 and yours is 07956738456")
entry_2 = DiaryEntry("This Title", "My new number is 07956247381")
diary.add(entry_1)
diary.add(entry_2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() == ["07956247381", "07956738456"]

"""
When I add one diary entry that fits the time, 
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it gets that diary entry
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "one two three four")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) == entry_1

"""
When I add one diary entry that does not fit in the time, 
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns none
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "one two three four five")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) == None

"""
When I add multiple diary entries, one readable
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns the readable one
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "one two three four five")
entry_2 = DiaryEntry("This Title", "one two three four ")
diary.add(entry_1)
diary.add(entry_2)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=2, minutes=2) == entry_2

"""
When I add multiple diary entries, multiple readable
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns the longest readable one
"""
diary = Diary()
entry_1 = DiaryEntry("This Title", "one two three four five")
entry_2 = DiaryEntry("This Title", "one two three four ")
entry_3 = DiaryEntry("This Title", "one two three four five six")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=3, minutes=2) == entry_3

"""
When I add no diary entries
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns None
"""
diary = Diary()
extractor = ReadableEntryExtractor(diary)
extractor.extract(wpm=3, minutes=2) == None


4. Create Examples as Unit Tests

Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE
# Diary
"""
Initially, Diary has no entries
"""
diary = Diary()
diary.all() == []

# DiaryEntry
"""
DiaryEntry is contrcuted with a title and contents
"""
entry = DiaryEntry()
entry.title = "My Title"
entry.contents = "My contents"

# TaskList
"""
Initially, TaskList has no incomplete tasks
"""
task_list = TaskList()
task_list.all_incomplete() == []

"""
When TaskList has no complete tasks
"""
task_list = TaskList()
task_list.all_complete() == []

# Task
"""
Initially, Task contrcust with title
"""
task = Task("Walk the dog")
task.title == "Walk the dog"


5. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.