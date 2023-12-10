from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Iterable

StopRule = Callable[[list[int]], bool]
AccumulateOperator = Callable[[int, int], int]
CombineOperator = Callable[[int, int], int]


def combine_consecutive_pairs(lst: list[int], op: CombineOperator) -> list[int]:
    result = []
    for i in range(len(lst)-1):
        result.append(op(lst[i], lst[i+1]))
    return result


def difference_accumulate(it: Iterable[int]) -> int:
    res = 0
    for v in it:
        res = v - res
    return res


@dataclass
class Reading:
    values: list[int]


    def get_prediction(self, stop_rule: StopRule, combine: CombineOperator, accumulate: AccumulateOperator) -> int:
        rows = [self.values]
        current = self.values

        while stop_rule(current):
            next_row = combine_consecutive_pairs(current, combine)
            rows.append(next_row)
            current = next_row
        
        return accumulate(r[0] for r in rows[::-1][1::])
    
    @staticmethod
    def loads(s: str, is_reversed: bool = True) -> Reading:
        read_seq = s.strip().split()[::-1] if is_reversed else s.strip().split()
        return Reading([int(r) for r in read_seq])

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    ops_p1 = {
        'stop_rule': lambda current : current[0] != 0,
        'combine': int.__sub__,
        'accumulate': sum
    }

    ops_p2 = {
        'stop_rule': lambda current : any(i != 0 for i in current),
        'combine': lambda x, y: y - x,
        'accumulate': difference_accumulate
    }

    print(f'part1 total = {sum(Reading.loads(l.strip()).get_prediction(**ops_p1) for l in lines if len(l))}')
    print(f'part2 total = {sum(Reading.loads(l.strip(), False).get_prediction(**ops_p2) for l in lines if len(l))}')