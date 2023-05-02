import pytest
from lib.diary import *

"""
Initially this has an empty list of entries
"""
def test_starts_with_empty_list():
    diary = Diary()
    assert diary.all() == []

"""
reading time raises an error if no entries are added
"""
def test_no_entries_added_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    error_message = str(e.value)
    assert error_message == "No entries added."

"""
find best entry for reading time raises an error if no entries are added
"""
def test_no_entries_added_raises_exception_for_best_entry():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(2,2)
    error_message = str(e.value)
    assert error_message == "No entries added."