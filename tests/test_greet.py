from lib.greet import *

def test_greet_returns_name():
    result = greet("Ilhaam")
    assert result == "Hello, Ilhaam!"