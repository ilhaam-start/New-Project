from lib.report_length import *

# This tests for word "hello"
def tests_hello_returns_five():
    result = report_length("hello")
    assert result == "This string was 5 characters long."

#tests for spaces
def tests_multiple_words():
    result = report_length("That's rough, buddy.")
    assert result == "This string was 20 characters long."