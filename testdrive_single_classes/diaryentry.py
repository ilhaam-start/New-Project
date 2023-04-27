import math
class DiaryEntry():
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.words_read = 0


    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        formatted = f"{self.title}: {self.contents}"
        return formatted

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())
        # Returns:
        #   int: the number of words in the diary entry


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if self.count_words() == 2:
            return  1
        else:
            return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        no_of_words = wpm * minutes
        string_list = self.format().split()
        words_available = self.count_words()

        if self.words_read > words_available:
            self.words_read = 0

        start_chunk = self.words_read
        end_chunk = no_of_words
        reading_chunks = string_list[start_chunk:end_chunk]
        print(f"Before it update, words read is: {self.words_read}")
        self.words_read += end_chunk
        print(f"After it update, words read is: {self.words_read}")
        print(no_of_words)
        words_available -= self.words_read
        return reading_chunks
    


diaryentry = DiaryEntry("Title", "one two three four five six seven")
print(diaryentry.format())
print(diaryentry.count_words())
print(diaryentry.reading_time(1))
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(2, 1))

# "Title", " ".join(["contents" for i in range(0, 100)