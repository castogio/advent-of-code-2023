import pytest

from day8 import *

def test_get_circular_directions():
    m = Map('LLR', None ,  {}) # type: ignore
    last = ''
    ns_gen = m.get_next_step_generator()
    for _ in range(6):
        last = next(ns_gen)
    assert last == 'R'

def test_parse_node_string():
    expected = Node('AAA', left='BBB', right='CCC')
    assert Node.loads('AAA = (BBB, CCC)') == expected

    expected = Node('ZZZ', left='ZZZ', right='ZZZ')
    assert Node.loads('ZZZ = (ZZZ, ZZZ)') == expected

def test_parse_wrong_node_string():

    with pytest.raises(ValueError):
        Node.loads('aaa = (aaa, aaa)')

    with pytest.raises(ValueError):
        Node.loads('aaa = (aaa aaa)')
    
    with pytest.raises(ValueError):
        Node.loads('aaa = (aaa, aaa')

def test_parse_maps_string():
    map_str = """RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)"""

    m = Map.loads(map_str.splitlines())

    assert m.steps == 'RL'
    assert len(m.nodes) == 7
    assert m.nodes['AAA'] == Node('AAA', left='BBB', right='CCC')
    assert m.nodes['ZZZ'] == Node('ZZZ', left='ZZZ', right='ZZZ')


def test_compute_sample_path():
    map_str = """RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)"""

    m = Map.loads(map_str.splitlines())
    assert len(m.compute_path()) == 2
    assert m.compute_path() == 'AAA CCC'.split()

def test_count_path_lenght_circular():
    map_str = """LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)"""

    m = Map.loads(map_str.splitlines())
    assert len(m.compute_path()) == 6


def test_find_paralles_start_nodes():
    map_str = """LR

    KKA = (KKB, XXX)
    KKB = (XXX, KKZ)
    KKZ = (KKB, XXX)
    JJA = (JJB, XXX)
    JJB = (JJC, JJC)
    JJC = (JJZ, JJZ)
    JJZ = (JJB, JJB)
    XXX = (XXX, XXX)"""

    assert [n.name for n in Map.loads(map_str.splitlines()).get_parallel_start_nodes()] == ['KKA', 'JJA']

def test_get_parallel_paths_lenght():
    map_str = """LR

    KKA = (KKB, XXX)
    KKB = (XXX, KKZ)
    KKZ = (KKB, XXX)
    JJA = (JJB, XXX)
    JJB = (JJC, JJC)
    JJC = (JJZ, JJZ)
    JJZ = (JJB, JJB)
    XXX = (XXX, XXX)"""

    m = Map.loads(map_str.splitlines())
    assert m.get_parallel_paths_lenght() == 6


def test_compute_sample_result():
    pass