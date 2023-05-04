from unittest.mock import Mock
import pytest
from lib.track import *


#If title and artist are given and we search keyword for partial track, matches is returns True
def test_keyword_matches_full_artist_returns_true():
    track = Track("my song", "Fav artist")
    assert track.matches("Fav artist") == True

#If title and artist are given and we search keyword for full track, matches is returns True
def test_keyword_matches_partial_artist_returns_true():
    track = Track("my song", "Fav artist")
    assert track.matches("Fav") == True

#If title and artist are given and we search keyword for full song, matches is returns True
def test_keyword_matches_full_song_returns_true():
    track = Track("my song", "Fav artist")
    assert track.matches("my song") == True

#If title and artist are given and we search keyword for partial song, matches is returns True
def test_keyword_matches_partial_song_returns_true():
    track = Track("my song", "Fav artist")
    assert track.matches("my") == True

#If title and artist are given and we search keyword not in track matches returns False
def test_keyword_does_not_match_return_false():
    track = Track("my song", "Fav artist")
    assert track.matches("Taylor") == False
