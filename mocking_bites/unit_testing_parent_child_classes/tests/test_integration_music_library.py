from lib.music_library import *
from lib.track import *

#Add multiple track tests if they are added in the Music Library, returns list
def test_multiple_tracks_added_returned_in_list():
    musiclibrary = MusicLibrary()
    track_1 = Track("song 1", "singer 1")
    track_2 = Track("song 2", "singer 2")
    track_3 = Track("song 3", "singer 3")
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    musiclibrary.add(track_3)
    assert musiclibrary.music_library == [track_1, track_2, track_3]

#Add one track tests if the keyword song is in the Music Library, when search is called return the match.
def test_keyword_in_song_title_return_true():
    musiclibrary = MusicLibrary()
    track_1 = Track("song 1", "singer 1")
    musiclibrary.add(track_1)
    assert musiclibrary.search("song") == [track_1]


#Add two tracks tests if the word keyword is in the Music Library, return match
def test_add_two_tracks_search_artist_return_true():
    musiclibrary = MusicLibrary()
    track_1 = Track("song 1", "singer 1")
    track_2 = Track("A whole new world", "Aladdin")
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    assert musiclibrary.search("Aladdin") == [track_2]

#Add two tracks tests if partial amount of keyword in the song is in the Music Library, return match
def test_add_two_tracks_search_partial_song_return_true():
    musiclibrary = MusicLibrary()
    track_1 = Track("song 1", "singer 1")
    track_2 = Track("A whole new world", "Aladdin")
    musiclibrary.add(track_1)
    musiclibrary.add(track_2)
    assert musiclibrary.search("A whole") == [track_2]
