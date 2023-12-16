import pytest

from day16 import *

# @pytest.fixture
# def test_map() -> Map:
#     print("Running setup method...")
#     with open('./input.txt') as f:
#         m = Map.loads(f.read())
    
#     yield m

#     # Teardown code
#     # nothing to do here


def test_straight_hor_movement():
    sample_map = '...............'
    m = Map.loads(sample_map)
    m.add_player(Player(0, 1, Position(0,0), None))
    m.play()
    assert all(t.energized for t in m.grid[0])

def test_straight_ver_movement():
    sample_map = '''.
                    .
                    .
                    .'''
    m = Map.loads(sample_map)
    m.add_player(Player(1, 0, Position(0,0), None))
    m.play()
    assert all(t.energized for row in m.grid for t in row)

def test_mirrors1():
    sample_map = '''.\.
                    .\.'''
    m = Map.loads(sample_map)
    p = Player(0, 1, Position(0,0), None)
    m.add_player(p)
    m.play()
    assert p.position == Position(x=3, y=1)

def test_mirrors2():
    sample_map = '''./'''
    m = Map.loads(sample_map)
    p = Player(0, 1, Position(0,0), None)
    m.add_player(p)
    m.play()
    assert p.position == Position(x=1, y=-1)


def test_ver_splitter():
    sample_map = '''.|.
                    .|.
                    .-.'''
    m = Map.loads(sample_map)
    p = Player(0, 1, Position(0,0), None)
    m.add_player(p)
    m.play()

    assert m.grid[2][0].energized
    assert m.grid[2][2].energized

