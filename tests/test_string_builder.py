from lib.string_builder import *

#tests if string size is correct
def tests_string_size_hello():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    assert stringbuilder.size() == 5

#tests if adding a string outpits the string.
def tests_string_output_hello():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    assert stringbuilder.output() == "hello"

#tests if multiple strings can be added
def tests_string_multiple_output_hello():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    stringbuilder.add(" goodbye")
    assert stringbuilder.output() == "hello goodbye"
