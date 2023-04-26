import pytest
from lib.make_snippet import *

#test for a sentence with more than five words
def test_make_snippet():
    sentences = make_snippet("There is a house on a hill") 
    assert sentences == "There is a house on..."

#test for a sentence with less than 5 words
def test_make_snippet_Less_than_five():
    sentences = make_snippet("Python is fun!")
    assert sentences == "Python is fun!"

def test_make_snippet_five_words():
    sentences = make_snippet("I have a small house")
    assert sentences == "I have a small house..."



