from lib.music_library import *

"""
Initially there are no tracks
"""
def test_no_tracks_added():
    musiclibrary = MusicLibrary()
    assert musiclibrary.all() == []

"""
Initially searching for tracks gets an empty list
"""
def test_search_returns_empty():
    musiclibrary = MusicLibrary()
    assert musiclibrary.search_by_title("hello") == []