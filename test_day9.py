import pytest

from day9 import *


# def test_op_consecutive_pairs():
#     assert op_consecutive_pairs([15, 12, 9, 6, 3, 0], int.__sub__) == [3, 3, 3, 3, 3]
#     assert op_consecutive_pairs([3, 3, 3, 3, 3], int.__sub__) == [0, 0, 0, 0]

def test_reading_loads():
    assert Reading.loads('0 3 6 9 12 15') == Reading([15, 12, 9, 6, 3, 0])
    assert Reading.loads('0 3 6 9 12 15', is_reversed=False) == Reading([0, 3, 6, 9, 12, 15])

def test_reading_get_part1_prediction():
    assert Reading([15, 12, 9, 6, 3, 0]).get_part1_prediction() == 18
    assert Reading([21, 15, 10, 6, 3, 1]).get_part1_prediction() == 28
    assert Reading([45, 30, 21, 16, 13, 10]).get_part1_prediction() == 68

def test_reading_get_part2_prediction():
    assert Reading([10, 13, 16, 21, 30, 45]).get_part2_prediction() == 5
    assert Reading.loads('0 3 6 9 12 15', False).get_part2_prediction() == -3
    assert Reading.loads('1 3 6 10 15 21', False).get_part2_prediction() == 0
    

def test_compute_sample_p1_total():
    sample = '''
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45'''

    assert sum(Reading.loads(l.strip()).get_part1_prediction() for l in sample.splitlines() if len(l)) == 114