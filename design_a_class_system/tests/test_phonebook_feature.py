"""
When I add multiple diary entries, 
And I call #PhoneNumberExtractor
I get a list of phone numbers from all diary entries
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "My number is 07956247381 and yours is 07956738456")
# entry_2 = DiaryEntry("This Title", "My contents 2")
# entry_3 = DiaryEntry("This Title", "My new number is 07547823459")
# diary.add(entry_1)
# diary.add(entry_2)
# diary.add(entry_3)
# extractor = PhoneNumberExtractor(diary)
# extractor.extract() == ["07956247381", "07956738456", "07547823459"]

"""
When I add a diary entry, 
And I call #PhoneNumberExtractor
it ignores invalid phone numbers
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "My number is 07956247381 and yours is 07956738456, 0794567")
# diary.add(entry_1)
# extractor = PhoneNumberExtractor(diary)
# extractor.extract() == ["07956247381", "07956738456"]

"""
When I add no diary entries
and I call Phone numberExtractor
it returns an empty list []
"""
# diary = Diary()
# extractor = PhoneNumberExtractor(diary)
# extractor.extract() == []

"""
When I add multiple diary entries, 
And I call #PhoneNumberExtractor
It ignores duplicate numbers
"""
# diary = Diary()
# entry_1 = DiaryEntry("This Title", "My number is 07956247381 and yours is 07956738456")
# entry_2 = DiaryEntry("This Title", "My new number is 07956247381")
# diary.add(entry_1)
# diary.add(entry_2)
# extractor = PhoneNumberExtractor(diary)
# extractor.extract() == ["07956247381", "07956738456"]