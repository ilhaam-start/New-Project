from lib.check_codeword import *

#If the code word is correct:

def tests_codeword_returns_answer():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

#if the codeword is incorrect:
def tests_incorrect_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"

#If first and last letter are correct:
def tests_some_correct_letters():
    result = check_codeword("house")
    assert result == "Close, but nope."