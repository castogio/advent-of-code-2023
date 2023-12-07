import pytest

from day7 import *

def test_create_hand():
    assert Hand.from_str('32T3K 765').cards == [3, 2, 10, 3, 12]

def test_parse_sample_hands():
    assert Hand.from_str('AAAAA 0').strength == Strenght.five_kind
    assert Hand.from_str('AA8AA 0').strength == Strenght.four_kind
    assert Hand.from_str('23332 0').strength == Strenght.full_house
    assert Hand.from_str('TTT98 0').strength == Strenght.three_kind
    assert Hand.from_str('23432 0').strength == Strenght.two_pair
    assert Hand.from_str('A23A4 0').strength == Strenght.one_pair
    assert Hand.from_str('23456 0').strength == Strenght.high_card

def test_joker_combos():
    assert Hand.from_str('2222J 0').strength == Strenght.five_kind
    assert Hand.from_str('222JJ 0').strength == Strenght.five_kind
    assert Hand.from_str('222J3 0').strength == Strenght.four_kind
    assert Hand.from_str('J22J3 0').strength == Strenght.four_kind
    assert Hand.from_str('JJ243 0').strength == Strenght.three_kind
    assert Hand.from_str('J2345 0').strength == Strenght.one_pair
    assert Hand.from_str('JJ345 0').strength == Strenght.three_kind
    assert Hand.from_str('JJJ45 0').strength == Strenght.four_kind

def test_compute_sample_result():
    
    test_entries = '''
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483'''

    test_cards = sorted(Hand.from_str(c.strip()) for c in test_entries.splitlines() if len(c))
    assert sum(rank * h.bid for rank, h in enumerate(test_cards, start=1)) == 5905


