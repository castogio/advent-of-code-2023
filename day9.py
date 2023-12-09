from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

def op_consecutive_pairs(lst: list[int], op: Callable) -> list[int]:
    result = []
    for i in range(len(lst)-1):
        result.append(op(lst[i], lst[i+1]))
    return result

@dataclass
class Reading:
    values: list[int]

    def get_part1_prediction(self) -> int:
        rows = [self.values]
        current = self.values

        while current[0] != 0:
            next_row = op_consecutive_pairs(current, int.__sub__)
            rows.append(next_row)
            current = next_row

        rows = rows[::-1]

        return sum(r[0] for r in rows[1::])
    
    @staticmethod
    def loads(s: str) -> Reading:
        return Reading([int(r) for r in s.strip().split()[::-1]])

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'part1 total = {sum(Reading.loads(l.strip()).get_part1_prediction() for l in lines if len(l))}')