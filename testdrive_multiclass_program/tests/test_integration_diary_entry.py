from lib.diary import *
from lib.diary_entry import *

"""
First, when I add a multiple diary entries, it returns a list with all my entries
"""
def test_multiple_entries_returns_adds_all():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here.")
    entry_2 = DiaryEntry("Second entry", "This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting.")
    entry_3 = DiaryEntry("Last entry", "wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story, wow what a great story")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.all() == [entry_1, entry_2, entry_3]

"""
If I add two diary entries,
I get the number of words in the contents of the entries.
"""
def test_add_entries_return_word_count_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here.")
    entry_2 = DiaryEntry("Second entry", "This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting. This is even more exciting.")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 76

"""
Given I add two diary entries with a total length of 7
And I call a reading time with wpm of 2
then the total reading time should be 4
"""
def test_reading_time_returns_time_to_read_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "Pretend I've written")
    entry_2 = DiaryEntry("Second entry", "This is even more")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 4

"""
Given I add one diary entry, 
and I call find_best_entry_for_reading_time with wpm and minutes that means I can read that entry
return the entry
"""
def test_entry_returned_for_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("Second entry", "This is even more than the first one")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_1

"""
Given I add one diary entry, 
and I call find_best_entry_for_reading_time with wpm and minutes that means I cannot read that entry
return None
"""
def test_entry_returns_none_for_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("Second entry", "This is even more than the first one")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None


"""
First, when I add a multiple diary entries, this will return the entry that is closest
to the length that the user could read in the minutes they have available. 
I will use a wpm and minute that is closer to the shorter string.
"""
def test_best_entry_for_reading_time_returns_shorter_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "Pretend I've written")
    entry_2 = DiaryEntry("Second entry", "This is even more than the first one")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given I add two diary entries, 
and I call find_best_entry_for_reading_time with wpm and minutes that means I can read both
return the longer one
"""
def test_best_entry_for_reading_time_returns_longer_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "Pretend I've written")
    entry_2 = DiaryEntry("Second entry", "This is even more than the first one")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2