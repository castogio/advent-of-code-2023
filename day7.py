
from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum
from collections import Counter

class Strenght(IntEnum):
    high_card = 0
    one_pair = 1
    two_pair = 2
    three_kind = 3
    full_house = 4
    four_kind = 5
    five_kind = 6
    not_computed = -1


card_mappings = dict(zip('A K Q T'.split(), range(13, 9, -1)))
card_mappings['J'] = 1
               
@dataclass
class Hand:
    cards: list[int]
    bid: int
    _strength: Strenght = Strenght.not_computed

    def __lt__(self, o: Hand) -> bool:
        if self.strength != o.strength:
            return self.strength < o.strength
        for c1, c2 in zip(self.cards, o.cards):
            if c1 != c2:
                return c1 < c2
        return False
    
    @property
    def strength(self) -> int:
        if self._strength is not Strenght.not_computed:
            return self._strength
        counter = Counter(self.cards)
        num_groups = len(counter.keys())
        num_jokers = counter.get(card_mappings['J'], 0)
        
        match num_groups:
            case 5:
                self._strength = Strenght.one_pair if num_jokers else Strenght.high_card
            case 4:
                self._strength = Strenght.three_kind if num_jokers else Strenght.one_pair
            case 3:
                self._strength = Strenght.three_kind if any(c == 3 for c in counter.values()) else Strenght.two_pair
                if num_jokers:
                    if self._strength == Strenght.three_kind:
                        self._strength = Strenght.four_kind
                    else:
                        self._strength = Strenght.full_house if num_jokers == 1 else Strenght.four_kind
            case 2:
                self._strength = Strenght.four_kind if any(c == 4 for c in counter.values()) else Strenght.full_house
                if num_jokers:
                    if self._strength == Strenght.four_kind:
                        self._strength = Strenght.five_kind
                    else:
                        self._strength = Strenght.full_house if num_jokers == 1 else Strenght.five_kind
            case 1:
                self._strength = Strenght.five_kind

        return self._strength
    
    @staticmethod
    def from_str(entry: str):
        cards_str, bid_str = entry.split()
        cards = []
        for c in cards_str:
            cards.append(int(c) if c not in card_mappings else card_mappings[c])
        return Hand(cards, int(bid_str))


if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    cards = sorted(Hand.from_str(c.strip()) for c in lines if len(c))
    print(f'total part 2 = {sum(rank * h.bid for rank, h in enumerate(cards, start=1))}')
