import pytest

from day14 import *

def test_shift_north():
    sample = '''O....#....
                O.OO#....#
                .....##...
                OO.#O....O
                .O.....O#.
                O.#..O.#.#
                ..O..#O..O
                .......O..
                #....###..
                #OO..#....'''
    
    sample_matrix: Matrix = [list(l.strip()) for l in sample.splitlines()]
    
    expect = '''OOOO.#.O..
                OO..#....#
                OO..O##..O
                O..#.OO...
                ........#.
                ..#....#.#
                ..O..#.O.O
                ..O.......
                #....###..
                #....#....'''
    
    expected_matrix: Matrix = [list(l.strip()) for l in expect.splitlines()]

    assert shift_vertical(sample_matrix) == expected_matrix

def test_compute_points():
    sample = '''OOOO.#.O..
                OO..#....#
                OO..O##..O
                O..#.OO...
                ........#.
                ..#....#.#
                ..O..#.O.O
                ..O.......
                #....###..
                #....#....'''
    
    m: Matrix = [list(l.strip()) for l in sample.splitlines()]
    assert compute_points(m) == 136

def test_shift_west():
    sample = '''OOOO.#.O..
                OO..#....#
                OO..O##..O
                O..#.OO...
                ........#.
                ..#....#.#
                ..O..#.O.O
                ..O.......
                #....###..
                #....#....'''
    
    m: Matrix = [list(l.strip()) for l in sample.splitlines()]

    expect = '''OOOO.#O...
                OO..#....#
                OOO..##O..
                O..#OO....
                ........#.
                ..#....#.#
                O....#OO..
                O.........
                #....###..
                #....#....'''
    
    expected_matrix: Matrix = [list(l.strip()) for l in expect.splitlines()]
    assert shift_horizontal(m, True) == expected_matrix

def test_shift_south():
    sample = '''OOOO.#O...
                OO..#....#
                OOO..##O..
                O..#OO....
                ........#.
                ..#....#.#
                O....#OO..
                O.........
                #....###..
                #....#....'''
    
    m: Matrix = [list(l.strip()) for l in sample.splitlines()]

    expect = '''.....#....
                ....#.O..#
                O..O.##...
                O.O#......
                O.O....O#.
                O.#..O.#.#
                O....#....
                OO....OO..
                #O...###..
                #O..O#....'''
    
    expected_matrix: Matrix = [list(l.strip()) for l in expect.splitlines()]

    assert shift_vertical(m, False) == expected_matrix

def test_shift_east():
    sample = '''.....#....
                ....#.O..#
                O..O.##...
                O.O#......
                O.O....O#.
                O.#..O.#.#
                O....#....
                OO....OO..
                #O...###..
                #O..O#....'''
    m: Matrix = [list(l.strip()) for l in sample.splitlines()]

    expect = '''.....#....
                ....#...O#
                ...OO##...
                .OO#......
                .....OOO#.
                .O#...O#.#
                ....O#....
                ......OOOO
                #...O###..
                #..OO#....'''
    
    expected_matrix: Matrix = [list(l.strip()) for l in expect.splitlines()]

    new_m = shift_horizontal(m, False)

    pprint.pprint(new_m)
    assert new_m == expected_matrix


def test_cycle():
    sample = '''O....#....
                O.OO#....#
                .....##...
                OO.#O....O
                .O.....O#.
                O.#..O.#.#
                ..O..#O..O
                .......O..
                #....###..
                #OO..#....'''
    sample_matrix: Matrix = [list(l.strip()) for l in sample.splitlines()]

    expect = '''.....#....
                ....#...O#
                ...OO##...
                .OO#......
                .....OOO#.
                .O#...O#.#
                ....O#....
                ......OOOO
                #...O###..
                #..OO#....'''
    
    expected_matrix: Matrix = [list(l.strip()) for l in expect.splitlines()]

    res = cycle(sample_matrix)
    # pprint.pp(res)
    assert res == expected_matrix


def test_3_cycles():
    sample = '''O....#....
                O.OO#....#
                .....##...
                OO.#O....O
                .O.....O#.
                O.#..O.#.#
                ..O..#O..O
                .......O..
                #....###..
                #OO..#....'''
    sample_matrix: Matrix = [list(l.strip()) for l in sample.splitlines()]

    expect = '''.....#....
                ....#...O#
                .....##...
                ..O#......
                .....OOO#.
                .O#...O#.#
                ....O#...O
                .......OOO
                #...O###.O
                #.OOO#...O'''
    
    expected_matrix: Matrix = [list(l.strip()) for l in expect.splitlines()]

    assert cycle_n_times(sample_matrix, 3) == expected_matrix


    
def test_1000000000_cycle():
    sample = '''O....#....
                O.OO#....#
                .....##...
                OO.#O....O
                .O.....O#.
                O.#..O.#.#
                ..O..#O..O
                .......O..
                #....###..
                #OO..#....'''
    sample_matrix: Matrix = [list(l.strip()) for l in sample.splitlines()]
    assert compute_p2_points(sample_matrix, 1_000_000_000) == 64



