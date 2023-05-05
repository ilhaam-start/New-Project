import pytest
from lib.secret_diary import *
from unittest.mock import Mock

"""
First we test that the secret diary can be unlocked with a mock and read
"""
def test_secret_diary_with_mock_can_be_unlocked_and_read():
    diary_mock = Mock() #a mock Diary instance
    diary_mock.read.return_value = "This is the beginning of my Diary"
    secretdiary = SecretDiary(diary_mock) #a SecretDiary instance with our mock
    secretdiary.unlock()
    assert secretdiary.read() == "This is the beginning of my Diary"


"""
We test that the secret diary starts off locked
"""
def test_secret_diary_with_mock_starts_off_locked():
    diary_mock = Mock() #a mock Diary instance
    diary_mock.read.return_value = "This is the beginning of my Diary"
    secretdiary = SecretDiary(diary_mock) #a SecretDiary instance with our mock
    with pytest.raises(Exception) as e:
        secretdiary.read()
    assert str(e.value) == "Go away!"


"""
We test that the secret diary can be locked after being unlocked with a mock
"""
def test_secret_diary_with_mock_can_be_locked():
    diary_mock = Mock()
    diary_mock.read.return_value = "This is the beginning of my Diary"
    secretdiary = SecretDiary(diary_mock)
    secretdiary.unlock()
    secretdiary.lock()
    with pytest.raises(Exception) as e:
        secretdiary.read()
    assert str(e.value) == "Go away!"

"""
We test that the #read() method of the mock Diary instance was called
"""
def test_mock_diary_read_method_called():
    diary_mock = Mock()
    diary_mock.read.return_value = "This is the beginning of my Diary"
    secretdiary = SecretDiary(diary_mock)
    secretdiary.unlock()
    assert secretdiary.read() == "This is the beginning of my Diary"
    diary_mock.read.assert_called_once()

"""
We test that the #read() method of the mock Diary instance was not called
"""
def test_mock_diary_read_method_not_called():
    diary_mock = Mock()
    diary_mock.read.return_value = "This is the beginning of my Diary"
    secretdiary = SecretDiary(diary_mock)
    with pytest.raises(Exception) as e:
        secretdiary.read()
    assert str(e.value) == "Go away!"
    diary_mock.read.assert_not_called()