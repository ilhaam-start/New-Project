import math

class DiaryEntry:

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.stop_off_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split()
        if self.stop_off_point >= len(words):
            self.stop_off_point = 0
        readable_chunk = wpm * minutes
        start_point = self.stop_off_point
        end_point = self.stop_off_point + readable_chunk
        amount_read = " ".join(words[start_point:end_point])
        self.stop_off_point += readable_chunk
        return amount_read
