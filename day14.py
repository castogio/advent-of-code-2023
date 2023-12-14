from __future__ import annotations
from copy import deepcopy
import pprint
from collections import defaultdict, Counter

Matrix = list[list[str]]

def transpose(m: Matrix) -> Matrix:
    result = [['' for _ in m] for row in range(len(m[0]))]
    for y, row in enumerate(m):
        for x, el in enumerate(row):
            result[x][y] = el
    return result

def shift_vertical(matrix: Matrix, is_north: bool = True) -> list[int]:
    result_matrix = deepcopy(matrix)
    op = int.__add__ if is_north else int.__sub__

    if is_north:
        obstacles = [0 if obs != '.' else -1 for obs in matrix[0]]
        to_scan = enumerate(matrix[1:], start=1)
    else:
        obstacles = [len(matrix)-1 if obs != '.' else len(matrix) for obs in matrix[len(matrix)-1]]
        to_scan = reversed(list(enumerate(matrix[:-1], start=0)))

    for y, row in to_scan:

        for x, el in enumerate(row):
            if el == 'O':
                new_y = op(obstacles[x], 1)
                # print(f'{x}, {y} --> {new_y}')
                result_matrix[y][x] = '.'
                result_matrix[new_y][x] = 'O'
                obstacles[x] = new_y
            else:
                if el == '#':
                    obstacles[x] = y
                result_matrix[y][x] = el

    return result_matrix

def shift_horizontal(matrix: Matrix, is_west: bool = True) -> list[int]:
    m_t = transpose(matrix)
    if is_west:
        return transpose(shift_vertical(m_t))
    return transpose(shift_vertical(m_t, False))

def cycle(m: Matrix) -> Matrix:
    north = shift_vertical(m, True)
    west = shift_horizontal(north, True)
    south = shift_vertical(west, False)
    return shift_horizontal(south, False)

def compute_points(m: Matrix) -> int:
    row_factor = len(m)
    total = 0
    for row in m:
        total += sum(1 for el in row if el == 'O') * row_factor
        row_factor -= 1
    return total

def cycle_n_times(m: Matrix, n: int) -> Matrix:
    new_m = deepcopy(m)
    for i in range(n):
        new_m = cycle(new_m)
    return new_m

def compute_p2_points(m: Matrix, max_iterations: int) -> int:
    t_m = deepcopy(m)
    previously_seen = []
    lowest_index = max_index = None
    duplicated = []
    for _ in range(max_iterations):
        t_m = cycle(t_m)
        if t_m not in previously_seen:
            previously_seen.append(t_m)
        else:
            duplicated.append(t_m)
            index = previously_seen.index(t_m)
            if index == lowest_index:
                break # the loop restarted
            if not lowest_index: 
                lowest_index = max_index = index
            if index > max_index:
                max_index = index

    loop_length = max_index - lowest_index + 1
    heading_not_repeated = [el for el in previously_seen if el not in duplicated]
    dup_index = (max_iterations - len(heading_not_repeated)) % loop_length
    return compute_points(duplicated[dup_index-1])


if __name__ == '__main__':
    
    with open('./input.txt') as f:
        m: Matrix = [list(l.strip()) for l in f.readlines()]

    m_shift_north = shift_vertical(m)
    print(f'part1 total = {compute_points(m_shift_north)}') # 108918
    print(f'part2 total = {compute_p2_points(m, 1_000_000_000)}') # 100310
    
    
