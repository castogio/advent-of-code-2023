import pytest

from day10 import *

def test_get_start_point():
    sample = '''..F7.
                .FJ|.
                SJ.L7
                |F--J
                LJ...'''

    assert Map.loads(sample.splitlines()).get_start_point() == Location(x=0,y=2)

def test_sample1():
    sample = '''.....
                .S-7.
                .|.|.
                .L-J.
                .....'''

    assert len(Map.loads(sample.splitlines()).compute_loop()) == 8

def test_sample2():
    sample = '''..F7.
                .FJ|.
                SJ.L7
                |F--J
                LJ...'''

    assert len(Map.loads(sample.splitlines()).compute_loop()) == 16

def test_get_inside_tiles_sample1():
    sample = '''...........
                .S-------7.
                .|F-----7|.
                .||.....||.
                .||.....||.
                .|L-7.F-J|.
                .|..|.|..|.
                .L--J.L--J.
                ...........'''
    assert len(Map.loads(sample.splitlines()).get_inside_tiles()) == 4

def test_get_inside_tiles_sample2():
    sample = '''..........
                .S------7.
                .|F----7|.
                .||....||.
                .||....||.
                .|L-7F-J|.
                .|..||..|.
                .L--JL--J.
                ..........'''
    assert len(Map.loads(sample.splitlines()).get_inside_tiles()) == 4

def test_get_inside_tiles_sample3():
    sample = '''.F----7F7F7F7F-7....
                .|F--7||||||||FJ....
                .||.FJ||||||||L7....
                FJL7L7LJLJ||LJ.L-7..
                L--J.L7...LJS7F-7L7.
                ....F-J..F7FJ|L7L7L7
                ....L7.F7||L7|.L7L7|
                .....|FJLJ|FJ|F7|.LJ
                ....FJL-7.||.||||...
                ....L---J.LJ.LJLJ...'''
    assert len(Map.loads(sample.splitlines()).get_inside_tiles()) == 8

def test_get_inside_tiles_sample4():
    sample = '''FF7FSF7F7F7F7F7F---7
                L|LJ||||||||||||F--J
                FL-7LJLJ||||||LJL-77
                F--JF--7||LJLJ7F7FJ-
                L---JF-JLJ.||-FJLJJ7
                |F|F-JF---7F7-L7L|7|
                |FFJF7L7F-JF7|JL---7
                7-L-JL7||F7|L7F-7F7|
                L.L7LFJ|||||FJL7||LJ
                L7JLJL-JLJLJL--JLJ.L'''
    assert len(Map.loads(sample.splitlines()).purge_unused_tiles().get_inside_tiles()) == 10




