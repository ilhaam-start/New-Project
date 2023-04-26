from lib.gratitudes import *

def test_first_add_returns_one_item():
    gratitude = Gratitudes()
    gratitude.add("the sun")
    result = gratitude.format()
    assert result == "Be grateful for: the sun"

def test_adding_item_returns_first_and_second():
    gratitude = Gratitudes()
    gratitude.add("the sun")
    gratitude.add("chocolate")
    result = gratitude.format()
    assert result == "Be grateful for: the sun, chocolate"