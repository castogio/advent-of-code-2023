import pytest

from day11 import *

def test_parse_input():
    sample = ['...#......',
              '.......#..']
    
    assert len(parse_input(sample)) == 2
    assert parse_input(sample)[0] == Galaxy(0, 3, 0)
    assert parse_input(sample)[1] == Galaxy(1, 7, 1)

def test_expand():

    sample = ['...#......',
              '.......#..']
    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 7, 1)]
    assert expand(galaxies) == [Galaxy(0, 3, 0), Galaxy(1, 10, 1)]

    sample = ['...#......',
              '..........',
              '..........',
              '....#.....']
    
    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 4, 3)]
    assert expand(galaxies) == [Galaxy(0, 3, 0), Galaxy(1, 4, 5)]

    sample = ['...#......',
              '.......#..',
              '..........',
              '#.........']

    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 7, 1), Galaxy(2, 0, 3)]
    assert expand(galaxies) == [Galaxy(0, 5, 0), Galaxy(1, 12, 1), Galaxy(2, 0, 4)]


def test_expand_factor():
    sample = ['...#......',
              '.......#..']
    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 7, 1)]
    assert expand(galaxies, factor=10) == [Galaxy(0, 3, 0), Galaxy(1, 34, 1)]

    sample = ['...#......',
              '..........',
              '..........',
              '....#.....']
    
    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 4, 3)]
    assert expand(galaxies, 10) == [Galaxy(0, 3, 0), Galaxy(1, 4, 23)]

    sample = ['...#......',
              '.......#..',
              '..........',
              '#.........']

    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 7, 1), Galaxy(2, 0, 3)]
    assert expand(galaxies, 10) == [Galaxy(0, 23, 0), Galaxy(1, 57, 1), Galaxy(2, 0, 4)]

def test_compute_path_lenghts():
    sample = ['...#......',
              '.......#..']
    galaxies = [Galaxy(0, 3, 0), Galaxy(1, 7, 1)]
    assert compute_path_lenghts(galaxies)[0][0] == 5

def test_part1_sample():

    galaxies = [Galaxy(0, 1, 6), Galaxy(1, 5, 11)]
    assert compute_path_lenghts(galaxies)[0][0] == 9

    galaxies = [Galaxy(0, 4, 0), Galaxy(1, 9, 10)]
    assert compute_path_lenghts(galaxies)[0][0] == 15

    galaxies = [Galaxy(0, 0, 2), Galaxy(1, 12, 7)]
    assert compute_path_lenghts(galaxies)[0][0] == 17

    galaxies = [Galaxy(0, 0, 11), Galaxy(1, 5, 11)]
    assert compute_path_lenghts(galaxies)[0][0] == 5

    sample = '''...#......
                .......#..
                #.........
                ..........
                ......#...
                .#........
                .........#
                ..........
                .......#..
                #...#.....'''

    galaxies = expand(parse_input([l.strip() for l in sample.splitlines()]))
    assert sum(r[0] for r in compute_path_lenghts(galaxies)) == 374

    galaxies = expand(parse_input([l.strip() for l in sample.splitlines()]), factor=10)
    assert sum(r[0] for r in compute_path_lenghts(galaxies)) == 1030
