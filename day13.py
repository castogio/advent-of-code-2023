from __future__ import annotations
from dataclasses import dataclass
from pprint import pp

Matrix = list[list[str]]

def load_matrices(s: str) -> list[Matrix]:
    current = []
    matrices = [current]
    for l in s.splitlines():
        l = l.strip()
        if l == '':
            current = []
            matrices.append(current)
        else:
            current.append(list(l))
    return matrices

def transpose(m: Matrix) -> Matrix:
    result = [['' for _ in m] for row in range(len(m[0]))]
    for y, row in enumerate(m):
        for x, el in enumerate(row):
            result[x][y] = el
    return result

def find_symmetry_loc(m: Matrix) -> int:
    seen = [m[0]]
    last_candidate = 0
    for i, row in enumerate(m[1:], start=1):
        last_candidate += 1
        if seen[-1] == row:
            remainder = m[i:i+len(seen)]
            previus = m[max(0, i-len(remainder)):i]
            if remainder == list(reversed(previus)):
                return last_candidate
        seen.append(row)

    if last_candidate >= len(m)-1:
        return -1
    return last_candidate


# def find_symmetry_loc(m: Matrix) -> int:
#     base = 0
#     top = len(m) - 1

#     while base < len(m):
#         is_same = all(el1 == el2 for el1, el2 in zip(m[base], m[top]))
        
#         base += 1
#         if is_same:
#             if base == top:
#                     break
#             top -= 1

#     if base == len(m):
#         m = list(reversed(m))
#         base = 0
#         top = len(m) - 1

#         while base < len(m):
#             is_same = all(el1 == el2 for el1, el2 in zip(m[base], m[top]))
            
#             base += 1
#             if is_same:
#                 if base == top:
#                         break
#                 top -= 1
        
#         if base == len(m):
#             return -1
#         base = len(m) - base - 1

#     return base

def compute_p1_result(matrices: list[Matrix]) -> int:
    total = 0
    reflection_points = [(find_symmetry_loc(m), find_symmetry_loc(transpose(m))) for m in matrices]
    for rp in reflection_points:
        addition = rp[0]*100 if rp[0] != -1 else rp[1]
        print(f'({rp[0]},{rp[1]}) -> {addition}')
        total += addition
    return total

if __name__ == '__main__':
    with open('./input.txt') as f:
        # lines = [line.strip() for line in f.readlines()]
        matrices = load_matrices(f.read())

    print(f'part1 total = {compute_p1_result(matrices)}')

    # sample = '''#.##..##.
    #             ..#.##.#.
    #             ##......#
    #             ##......#
    #             ..#.##.#.
    #             ..##..##.
    #             #.#.##.#.'''
    
    # matrix = [list(l.strip()) for l in sample.splitlines()]
    # pp(matrix)
    # pp(transpose(matrix))

