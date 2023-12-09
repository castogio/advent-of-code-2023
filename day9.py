from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

@dataclass
class Reading:
    values: list[int]

    def get_part1_prediction(self) -> int:
        rows = [self.values]
        current = self.values

        def op_consecutive_pairs(lst: list[int]) -> list[int]:
            result = []
            for i in range(len(lst)-1):
                result.append(lst[i] - lst[i+1])
            return result

        while current[0] != 0:
            next_row = op_consecutive_pairs(current)
            rows.append(next_row)
            current = next_row

        rows = rows[::-1]
        return sum(r[0] for r in rows[1::])
    
    def get_part2_prediction(self) -> int:
        rows = [self.values]
        current = self.values

        def op_consecutive_pairs(lst: list[int]) -> list[int]:
            result = []
            for i in range(len(lst)-1):
                result.append(lst[i+1] - lst[i])
            return result

        while any(i != 0 for i in current):
            next_row = op_consecutive_pairs(current)
            rows.append(next_row)
            current = next_row

        rows = rows[::-1]
        res = 0
        for r in rows[1::]:
            res = r[0] - res
        return res
    
    @staticmethod
    def loads(s: str, is_reversed: bool = True) -> Reading:
        read_seq = s.strip().split()[::-1] if is_reversed else s.strip().split()
        return Reading([int(r) for r in read_seq])

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'part1 total = {sum(Reading.loads(l.strip()).get_part1_prediction() for l in lines if len(l))}')
    print(f'part2 total = {sum(Reading.loads(l.strip(), False).get_part2_prediction() for l in lines if len(l))}')