from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations

@dataclass
class Galaxy:
    id: int
    x: int
    y: int

def parse_input(lines: list[str]) -> list[Galaxy]:
    galaxies = []
    i = 0
    for y, l in enumerate(lines):
        for x, s in enumerate(l):
            if s == '#':
                galaxies.append(Galaxy(i, x, y))
                i += 1
    return galaxies

def expand(galaxies: list[Galaxy], factor: int = 2) -> list[Galaxy]:

    x_sorted = sorted(galaxies, key=lambda g: g.x)
    y_sorted = sorted(galaxies, key=lambda g: g.y)

    for i in range(len(x_sorted)-1):
        delta_x = x_sorted[i+1].x - x_sorted[i].x - 1
        if delta_x > 0:
            for g in x_sorted[i+1:]:
                g.x -= delta_x
                g.x += delta_x * factor

    for i in range(len(y_sorted)-1):
        delta_y = y_sorted[i+1].y - y_sorted[i].y - 1
        if delta_y > 0:
            for g in y_sorted[i+1:]:
                g.y -= delta_y
                g.y += delta_y * factor
    
    return galaxies

def compute_path_lenghts(galaxies: list[Galaxy]) -> list[tuple[int, Galaxy, Galaxy]]:
    result = []
    for g1, g2 in list(combinations(galaxies, 2)):
        result.append((abs(g1.x-g2.x)+abs(g1.y-g2.y), g1, g2))
    return result

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    galaxies = expand(parse_input([l.strip() for l in lines]))
    print(f'part 1 total = {sum(r[0] for r in compute_path_lenghts(galaxies))}')

    galaxies = expand(parse_input([l.strip() for l in lines]), factor=1_000_000)
    print(f'part 2 total = {sum(r[0] for r in compute_path_lenghts(galaxies))}')