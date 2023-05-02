from lib.diary_entry import *

"""
When I initialise with a title and contents, I get these back
"""
def test_constructs_gets_title_and_contents_back():
    diaryentry = DiaryEntry("My Title", "My Contents")
    assert diaryentry.title == "My Title"
    assert diaryentry.contents == "My Contents"

"""
If I put in one entry, this will return the number of words in its contents
"""
def test_return_no_of_words_in_contents():
    diaryentry = DiaryEntry("My Title", "Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here. Pretend I've written something interesting here.")
    assert diaryentry.count_words() == 36

"""
If I put in one entry, this will return the time taken to read this
"""
def test_one_entry_reading_time():
    diaryentry = DiaryEntry("My Title", "Pretend I've written something interesting here")
    assert diaryentry.reading_time(2) == 3

"""
when I initialise with a contents, then at first the reading chunk 
should return the first chunk readable in the time available
"""
def test_reading_chunk_returns_first_chunk_for_reading_time():
    diaryentry = DiaryEntry("My Title", "Pretend I've written something interesting here")
    assert diaryentry.reading_chunk(2,2) == "Pretend I've written something"

"""
when I initialise with a contents, then on the second call, reading chunk
should return the second chunk readable in the time available
"""
def test_reading_chunk_returns_first_chunk_for_reading_time():
    diaryentry = DiaryEntry("My Title", "Pretend I've written something interesting here")
    diaryentry.reading_chunk(2,2)
    assert diaryentry.reading_chunk(2,1) == "interesting here"

"""
when I initialise with a contents, then on the third call, reading chunk
should return the third chunk readable in the time available
"""
def test_reading_chunk_returns_first_chunk_for_reading_time():
    diaryentry = DiaryEntry("My Title", "Pretend I've written something interesting here, oh this is interesting")
    diaryentry.reading_chunk(2,2)
    diaryentry.reading_chunk(2,2)
    assert diaryentry.reading_chunk(2,1) == "is interesting"

"""
when I initialise with a contents, then on the fourth call, reading chunk
should restart from the beginning
"""
def test_reading_chunk_returns_first_chunk_for_reading_time():
    diaryentry = DiaryEntry("My Title", "Pretend I've written something interesting here, oh this is interesting")
    diaryentry.reading_chunk(2,2)
    diaryentry.reading_chunk(2,2)
    diaryentry.reading_chunk(2,1) 
    assert diaryentry.reading_chunk(2,1) == "Pretend I've"