from unittest.mock import Mock
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
def test_keyword_return_matching_track():
    musiclibrary = MusicLibrary()
    fake_match = Mock()
    fake_match.matches.return_value = True
    musiclibrary.add(fake_match)
    fake_non_match = Mock()
    fake_non_match.matches.return_value = False
    musiclibrary.add(fake_non_match)
    assert musiclibrary.search("hello") == [fake_match]

#If a single track is added and keyword searched, return matching track
def test_searches_by_keyword_with_single_tracks():
    musiclibrary = MusicLibrary()
    single_track = Mock()
    single_track.matches.return_value == True
    musiclibrary.add(single_track)
    assert musiclibrary.search("my song") == [single_track]

#initially music_library is empty
def test_empty_tracks():
    musiclibrary = MusicLibrary()
    assert musiclibrary.music_library == []

#when I add some tracks they show up in the list
def test_tracks_added_appear_in_list():
    musiclibrary = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    musiclibrary.add(track_3)
    assert musiclibrary.music_library == [track_1, track_2, track_3]