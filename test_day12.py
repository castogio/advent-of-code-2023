import pytest

from day12 import *

def test_is_valid():
    assert is_valid(list('#.#.###'), [1,1,3])
    assert is_valid(list('#....######..#####.'), [1,6,5])
    assert is_valid(list('.###.##....#'), [3,2,1])
    assert is_valid(list('#.#.###'), [1,1,3])

def test_count_valid_arrangement():
    assert Report.loads('???.### 1,1,3').count_valid_p1_arrangements() == 1
    assert Report.loads('.??..??...?##. 1,1,3').count_valid_p1_arrangements() == 4
    assert Report.loads('?#?#?#?#?#?#?#? 1,3,1,6').count_valid_p1_arrangements() == 1
    assert Report.loads('????.#...#... 4,1,1').count_valid_p1_arrangements() == 1
    assert Report.loads('????.######..#####. 1,6,5').count_valid_p1_arrangements() == 4
    assert Report.loads('?###???????? 3,2,1').count_valid_p1_arrangements() == 10

def test_part1_sample():
    sample = '''???.### 1,1,3
                .??..??...?##. 1,1,3
                ?#?#?#?#?#?#?#? 1,3,1,6
                ????.#...#... 4,1,1
                ????.######..#####. 1,6,5
                ?###???????? 3,2,1'''
    
    assert sum(Report.loads(s.strip()).count_valid_p1_arrangements() for s in sample.splitlines()) == 21

def test_is_still_valid():
    assert is_still_valid(list('#???.######..#####'), [1, 6, 5])

def test_count_valid_arrangement_expanded():
    assert Report.loads('???.### 1,1,3').expand().count_valid_p2_arrangements() == 1
    assert Report.loads('.??..??...?##. 1,1,3').expand().count_valid_p2_arrangements() == 16384
    # assert Report.loads('?#?#?#?#?#?#?#? 1,3,1,6').expand().count_valid_p2_arrangements() == 1
    # assert Report.loads('????.#...#... 4,1,1').expand().count_valid_p2_arrangements() == 1
    # assert Report.loads('????.######..#####. 1,6,5').count_valid_arrangements() == 4
    # assert Report.loads('?###???????? 3,2,1').count_valid_arrangements() == 10