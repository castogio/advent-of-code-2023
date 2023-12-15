import pytest

from day15 import *

def test_sample_hash():
    assert hash(Command('rn=1')) == 30
    assert hash(Command('qp=3')) == 97
    assert hash(Command('cm=2')) == 47
    assert hash(Command('qp-')) == 14
    assert hash(Command('pc=4')) == 180
    assert hash(Command('ot=7')) == 231

def test_compute_total_focal_len():

    sample = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
    commands: list[Command] = [Command(st) for st in sample.split(',')]
    
    map = HashMap()

    for c in commands:
        map.add(c)

    assert map.get_focusing_pwr() == 145
