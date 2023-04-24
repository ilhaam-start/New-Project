from lib.report_length import *

# This tests for word "hello"
def tests_hello_returns_five():
    result = report_length("hello")
    assert result == "This string was 5 characters long."

