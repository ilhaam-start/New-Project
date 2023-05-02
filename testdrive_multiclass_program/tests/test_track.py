from lib.track import *

"""
When I create a new track, I get the title and artist back
"""
def test_create_track_return_details():
    track = Track("My title", "The artist")
    assert track.title == "My title"
    assert track.artist == "The artist"

"""
When I create a new track, I get the title and artist back in new format
"""
def test_add_track_return_with_format():
    track = Track("My title", "The artist")
    assert track.format() == "My title by The artist"