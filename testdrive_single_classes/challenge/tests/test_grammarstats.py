import pytest
from lib.grammarstats import *

#Given that the text is an empty string, raise and error.
def test_empty_string():
    grammarstats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammarstats.check("")
    error_message = str(e.value)
    assert error_message == "There is no text, cannot check grammar."

#Given that the text begins with a capital and ends with a sentence-ending punctuation mark return True.
def test_capital_and_suitable_punction_return_true():
    grammarstats = GrammarStats()
    result = grammarstats.check("I have a dream.")
    assert result == True

#Given that the text beings with a capital letter but doed not end in a punctuation mark, return False.
def test_capital_start_return_false():
    grammarstats = GrammarStats()
    result = grammarstats.check("That one day")
    assert result == False

#Given that the text beings with a lowercase letter but does end in a punctuation mark, return False.
def test_lowercase_start_return_false():
    grammarstats = GrammarStats()
    result = grammarstats.check("i have a dream!")
    assert result == False

#Given that the text beings with a lowercase letter and does not end in a punctuation mark, return False.
def test_lowercase_start_no_punctuation_return_false():
    grammarstats = GrammarStats()
    result = grammarstats.check("that one day")
    assert result == False

#Given that the perecentage of text checked so far passes the check defined in the 'check' method, return the int percentage.
def test_that_text_has_correct_grammar_return_percentage_text_checked():
    grammarstats = GrammarStats()
    result = grammarstats.check("My name is Ilhaam, what is your name?")
    result = grammarstats.check("My name is Ilhaam, what is your name?")
    result = grammarstats.check("My name is Ilhaam, what is your name?")
    checker = grammarstats.percentage_good()
    assert checker == 100

#Given that the perecentage of text checked so far passes the check defined in the 'check' method, return the int percentage.
def test_correct_grammar_is_seventy_five_return_percentage_text_checked():
    grammarstats = GrammarStats()
    result = grammarstats.check("My name is Ilhaam what is your name.")
    result = grammarstats.check("My name is Ilhaam, what is your name?")
    result = grammarstats.check("My name is Ilhaam, what is your name?")
    result = grammarstats.check("My name is Ilhaam, what is your name")
    checker = grammarstats.percentage_good()
    assert checker == 75