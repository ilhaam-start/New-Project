import pytest
from lib.music_library import *

#If the Music Library is empty, when search is called, raise error
def test_keyword_not_in_music_library_raise_error():
    musiclibrary = MusicLibrary()
    with pytest.raises(Exception) as e:
        musiclibrary.search("drake") == False
    error_message = str(e.value)
    assert error_message == "No tracks in the music library."

#If multiple tracks added and keyword search, return matching track
# def test_keyword_return_matching_track():
#     musiclibrary = MusicLibrary()
#     fake_match = FakeMatchingTrack
#     fake_non_match = FakeNotMatchingTrack
#     musiclibrary.add(FakeMatchingTrack)
#     musiclibrary.add(FakeNotMatchingTrack)
#     assert musiclibrary.search("hello") == [fake_match]

# class FakeMatchingTrack:
#     def matches(self, keyword):
#         return True

# class FakeNotMatchingTrack:
#     def matches(self, keyword):
#         return False