from __future__ import annotations
from dataclasses import dataclass
from pprint import pp

def substitute(word: list[str]) -> list[list[str]]:
    if '?' not in word:
        return [''.join(word)]
    else:
        combinations = []
        index = word.index('?')

        for char in ['.', '#']:
            new_list = word.copy()
            new_list[index] = char
            combinations.extend(substitute(new_list))

        return combinations

def is_valid(word: list[str], group_counts: list[int]) -> bool:
    streak = 0
    sub_groups_counts = []

    for ch in word:
        if ch == '#':
            streak += 1
        else:
            if streak:
                sub_groups_counts.append(streak)
                streak = 0
    if streak:
        sub_groups_counts.append(streak)

    return sub_groups_counts == group_counts


def is_still_valid(word: list[str], group_counts: list[int]) -> bool:

    if '?' not in word:
        return is_valid(word, group_counts)
    
    num_fault = sum(1 for ch in word if ch == '#')
    num_exp = sum(group_counts)
    if num_fault > num_exp:
        return False

    streak = 0
    sub_groups_counts = []

    for ch in word:
        if ch == '?':
            break
        if ch == '#':
            streak += 1
        else:
            if streak:
                sub_groups_counts.append(streak)
                streak = 0
    if streak:
        sub_groups_counts.append(streak)

    for f, r in zip(sub_groups_counts[:-1], group_counts[:len(sub_groups_counts)-1]):
        if f > r:
            return False
    return True


def substitute_valid(word: list[str], group_counts: list[int]) -> list[list[str]]:

    if '?' not in word:
        return [''.join(word)] if is_valid(word, group_counts) else []
    else:
        combinations = []
        index = word.index('?')

        for char in ['.', '#']:
            new_list = word.copy()
            new_list[index] = char
            if is_still_valid(new_list, group_counts):
                combinations.extend(substitute_valid(new_list, group_counts))
        return combinations

@dataclass
class Report:
    condition: list[str]
    group_counts: list[int, int, int]

    def count_valid_p1_arrangements(self) -> int:
       combos = substitute(self.condition)
       return sum(1 for c in combos if is_valid(c, self.group_counts))
    
    def count_valid_p2_arrangements(self) -> int:
       combos = substitute_valid(self.condition, self.group_counts)
       return sum(1 for c in combos)
           
    def expand(self) -> Report:
        for _ in range(5):
            self.condition += ['?'] + self.condition
            self.group_counts +=  self.group_counts
        return self

    @staticmethod
    def loads(s: str) -> Report:
        conditions, group_counts = s.split()
        return Report(list(conditions), [int(v) for v in group_counts.split(sep=',')])

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'part 1 total = {sum(Report.loads(l).count_valid_p1_arrangements() for l in lines)}')
    