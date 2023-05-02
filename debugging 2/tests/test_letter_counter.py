from lib.letter_counter import *

#Test that the most common letter is correct
def test_most_common_letter_return_string():
    lettercounter = LetterCounter("Digital Punk")
    result = lettercounter.calculate_most_common()
    assert result == [2, "i"]