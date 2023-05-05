import pytest
from lib.secret_diary import *
from lib.diary import *

"""
Given that the diary has contents and it is locked, when
#read is called an error is raised that says "Go away!"
"""
def test_diary_locked_read_raises_error():
    secretdiary = SecretDiary(Diary("My contents"))
    with pytest.raises(Exception) as e:
        secretdiary.read()
    assert str(e.value) == "Go away!"

"""
Given that the diary has contents and it is unlocked, when
#read is called the contents are returned
"""
def test_diary_unlocked_read_returns_contents():
    secretdiary = SecretDiary(Diary("My contents"))
    secretdiary.unlock()
    assert secretdiary.read() == "My contents"


