import math

class Diary:

    def __init__(self):
        self.diaryentry = []

    def add(self, entry):
        self.diaryentry.append(entry)

    def all(self):
        return self.diaryentry

    def count_words(self):
        word_count = [entry.count_words() for entry in self.diaryentry]
        return sum(word_count)
            

    def reading_time(self, wpm):
        if self.diaryentry == []:
            raise Exception("No entries added.")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self.diaryentry == []:
            raise Exception("No entries added.")
        chunk_readable = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self.diaryentry:
            if entry.count_words() <= chunk_readable:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable
