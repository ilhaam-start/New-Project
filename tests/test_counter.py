from lib.counter import *

def test_increases_by_5():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_decreases_by_3():
    counter = Counter()
    counter.add(-3)
    result = counter.report()
    assert result == "Counted to -3 so far."