class MusicLibrary:
    
    def __init__(self):
        self.music_library = []

    def add(self, track):
        self.music_library.append(track)

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        if self.music_library == []:
            raise Exception("No tracks in the music library.")
        return [track for track in self.music_library if track.matches(keyword)]