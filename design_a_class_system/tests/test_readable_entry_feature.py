"""
When I add one diary entry that fits the time, 
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it gets that diary entry
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "one two three four")
# diary.add(entry_1)
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) == entry_1

"""
When I add one diary entry that does not fit in the time, 
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns none
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "one two three four five")
# diary.add(entry_1)
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) == None

"""
When I add multiple diary entries, one readable
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns the readable one
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "one two three four five")
# entry_2 = DiaryEntry("This Title", "one two three four ")
# diary.add(entry_1)
# diary.add(entry_2)
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=2, minutes=2) == entry_2

"""
When I add multiple diary entries, multiple readable
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns the longest readable one
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "one two three four five")
# entry_2 = DiaryEntry("This Title", "one two three four ")
# entry_3 = DiaryEntry("This Title", "one two three four five six")
# diary.add(entry_1)
# diary.add(entry_2)
# diary.add(entry_3)
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=3, minutes=2) == entry_3

"""
When I add no diary entries
and I call ReadableEntryExtractor with wpm of 2 and minutes 2
it returns None
"""
# diary = Diary()
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(wpm=3, minutes=2) == None