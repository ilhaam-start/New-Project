from lib.diary import *

"""
Initially the diary has no contents, returns empty string
"""
def test_no_contents_returns_empty_string():
    diary = Diary("")
    assert diary.read() == ""


"""
The diary has one content, returns the contents
"""
def test_one_content_return_string():
    diary = Diary("My diary starts here")
    assert diary.read() == "My diary starts here"