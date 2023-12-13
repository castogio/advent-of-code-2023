import pytest

from day13 import *


def test_load_matrices():

    sample = '''#.##..##.
                ..#.##.#.
                ##......#
                ##......#
                ..#.##.#.
                ..##..##.
                #.#.##.#.

                #...##..#
                #....#..#
                ..##..###
                #####.##.
                #####.##.
                ..##..###
                #....#..#'''

    matrices = load_matrices(sample)
    assert len(matrices) == 2


def test_transpose_matrix():
    sample = '''#.
                #.'''
    transposed = '''##
                    ..'''
    matrix = [list(l.strip()) for l in sample.splitlines()]
    result = [list(l.strip()) for l in transposed.splitlines()]
    assert transpose(matrix) == result

def test_find_symmetry_loc():
    sample = '''#.##..##.
                ..#.##.#.
                ##......#
                ##......#
                ..#.##.#.
                ..##..##.
                #.#.##.#.'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(transpose(matrix)) == 5

    sample = '''#.##..##.
                ..#.##.#.
                ##......#
                ##......#
                ..#.##.#.
                ..##..##.
                #.#.##.#.'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == -1 # out of range

    sample = '''#...##..#
                #....#..#
                ..##..###
                #####.##.
                #####.##.
                ..##..###
                #....#..#'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == 4

    sample = '''#...##..#
                #....#..#
                ..##..###
                #####.##.
                #####.##.
                ..##..###
                #....#..#'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(transpose(matrix)) == -1

def test_find_symmetry_loc_real_input():
    sample = '''#.###..#..###
                .#...##.####.
                .#...##.####.
                #.###..#..###
                .#######.##.#
                .#..##.#.#..#
                ..#..#.##.#..
                ##..##..###.#
                ######.##..#.
                ######.##....
                ##..##..###.#
                ..#..#.##.#..
                .#..##.#.#..#'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == 2

def test_find_symmetry_transposed():
    sample = '''#.##..##.
                ..#.##.#.
                ##......#
                ##......#
                ..#.##.#.
                ..##..##.
                #.#.##.#.'''
    
    matrix = transpose([list(l.strip()) for l in sample.splitlines()])
    assert find_symmetry_loc(matrix) == 5


def test_compute_p1_result():
    sample1 = '''#.##..##.
            ..#.##.#.
            ##......#
            ##......#
            ..#.##.#.
            ..##..##.
            #.#.##.#.'''
    matrix1 = [list(l.strip()) for l in sample1.splitlines()]
    
    sample2 = '''#...##..#
            #....#..#
            ..##..###
            #####.##.
            #####.##.
            ..##..###
            #....#..#'''
    matrix2 = [list(l.strip()) for l in sample2.splitlines()]
    
    matrices = [matrix1, matrix2]
    assert compute_p1_result(matrices) == 405

def test_compute_p2_result():
    sample1 = '''#.##..##.
                ..#.##.#.
                ##......#
                ##......#
                ..#.##.#.
                ..##..##.
                #.#.##.#.'''
    
    matrix1 = [list(l.strip()) for l in sample1.splitlines()]
    
    sample2 = '''#...##..#
                #....#..#
                ..##..###
                #####.##.
                #####.##.
                ..##..###
                #....#..#'''
    matrix2 = [list(l.strip()) for l in sample2.splitlines()]
    
    matrices = [matrix1, matrix2]
    assert compute_p2_result(matrices) == 400

def test_find_symmetry_smudge_loc_real_input():
    sample = '''#.###..#..###
                .#...##.####.
                .#...##.####.
                #.###..#..###
                .#######.##.#
                .#..##.#.#..#
                ..#..#.##.#..
                ##..##..###.#
                ######.##....
                ######.##....
                ##..##..###.#
                ..#..#.##.#..
                .#..##.#.#..#'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix)[1] == 9

def test_find_symmetry_smudge_loc_real_input():
    sample = '''#.###..#..###
                .#...##.####.
                .#...##.####.
                #.###..#..###
                .#######.##.#
                .#..##.#.#..#
                ..#..#.##.#..
                ##..##..###.#
                ######.##..#.
                ######.##....
                ##..##..###.#
                ..#..#.##.#..
                .#..##.#.#..#'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == 2
    assert find_symmetry_smudges(matrix) == 9

    sample = '''#......
                #......
                ....#..
                #.#.###
                #####..
                ###.##.
                ...#.##
                #.#.###
                ####.#.
                ..##..#
                ..##..#
                ####.#.
                #.#.###
                ...#.##
                ###.##.
                ###.#..
                #.#.###'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == 1
    assert find_symmetry_smudges(matrix) == 10

def test_overflow_smudge():
    sample = '''###.####..#.#
            #########.###
            #.####...#...
            #.####...#...
            ##.######.###
            ###.####..#.#
            ##.#..#.##...
            #..#.##.#...#
            ..#.########.
            ..#.########.
            #..#.##.#...#'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == 9
    assert find_symmetry_smudges(matrix) == 3

def test_avoid_null_null():
    sample = '''#####.###
                .#####.##
                ..#.#.###
                ..#.#.##.
                .#####.##
                #####.###
                ##.#....#
                #..##....
                #..##....'''
    
    matrix = [list(l.strip()) for l in sample.splitlines()]
    assert find_symmetry_loc(matrix) == 8
    assert find_symmetry_smudges(matrix) == 3



