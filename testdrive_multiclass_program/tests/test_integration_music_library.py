from lib.music_library import *
from lib.track import *

"""
When I add two tracks
I get the tracks back in the track list
"""
def test_adds_multiple_tracks_and_lists_them():
    musiclibrary = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    assert musiclibrary.all() == [track_1, track_2]

"""
Given I add two tracks, if I search for the title of one track
I get that track back in the results
"""
def test_search_one_track_return_track_in_result():
    musiclibrary = MusicLibrary()
    track_1 = Track("My title", "The artist")
    track_2 = Track("This track is", "I am an artist")
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    assert musiclibrary.search_by_title("My title") == [track_1]

"""
If I add two tracks, and I search part of the title of one track 
I get back the matching track
"""
def test_search_by_part_of_track():
    musiclibrary = MusicLibrary()
    track_1 = Track("My title", "The artist")
    track_2 = Track("This track is", "I am an artist")
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    assert musiclibrary.search_by_title("My") == [track_1]