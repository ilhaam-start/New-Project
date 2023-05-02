class MusicLibrary:

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)
    
    def all(self):
        return self.tracks

    def search_by_title(self, keyword):
        return [track for track in self.tracks if keyword in track.title]
        