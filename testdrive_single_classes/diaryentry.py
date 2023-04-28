import math
class DiaryEntry():
    def __init__(self, title, contents):

        self.title = title
        self.contents = contents
        self.words_read = 0


    def format(self):

        formatted = f"{self.title}: {self.contents}"
        return formatted

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())

    def reading_time(self, wpm):
        
        if self.count_words() == 2:
            return  1
        else:
            return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        
        no_of_words = wpm * minutes
        string_list = self.format().split()
        # words_available = self.count_words() - TURNS OUT WE DON'T NEED THIS

        if self.words_read >= len(string_list): #This is saying if the words read is greater than or equal to the length of our string list (so basically the words available) then bring the words ready back to zero.
            self.words_read = 0

        start_chunk = self.words_read #This is where we start reading
        end_chunk = self.words_read + no_of_words # We end the chunk by adding the number of words to the amount read
        reading_chunks = string_list[start_chunk:end_chunk] #This counts from the start chunk to the end chunk.
        print(f"Before it updates, words read is: {self.words_read}")
        self.words_read = end_chunk #Now the words read is equal to the end chunk, so that when we go back to the beginning it will say words read is now increased. (We didn't need to do self.words_read += end_chunk)
        print(f"After it updates, words read is: {self.words_read}")
        print(no_of_words)
        # words_available -= self.words_read
        return " ".join(reading_chunks) #Join the words so its not a list.
    


diaryentry = DiaryEntry("Title", "one two three four five six seven")
print(diaryentry.format())
print(diaryentry.count_words())
print(diaryentry.reading_time(1))
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(3, 1))
print(diaryentry.reading_chunk(2, 1))

# "Title", " ".join(["contents" for i in range(0, 100)