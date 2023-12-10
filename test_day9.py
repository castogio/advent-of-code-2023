import pytest

from day9 import *


def test_reading_loads():
    assert Reading.loads('0 3 6 9 12 15') == Reading([15, 12, 9, 6, 3, 0])
    assert Reading.loads('0 3 6 9 12 15', is_reversed=False) == Reading([0, 3, 6, 9, 12, 15])

def test_reading_get_part1_prediction():

    ops = {
        'stop_rule': lambda current : current[0] != 0,
        'combine': int.__sub__,
        'accumulate': sum
    }

    assert Reading([15, 12, 9, 6, 3, 0]).get_prediction(**ops) == 18
    assert Reading([21, 15, 10, 6, 3, 1]).get_prediction(**ops) == 28
    assert Reading([45, 30, 21, 16, 13, 10]).get_prediction(**ops) == 68

def test_reading_get_part2_prediction():

    ops = {
        'stop_rule': lambda current : any(i != 0 for i in current),
        'combine': lambda x, y: y - x,
        'accumulate': difference_accumulate
    }

    assert Reading([10, 13, 16, 21, 30, 45]).get_prediction(**ops) == 5
    assert Reading.loads('0 3 6 9 12 15', False).get_prediction(**ops) == -3
    assert Reading.loads('1 3 6 10 15 21', False).get_prediction(**ops) == 0
