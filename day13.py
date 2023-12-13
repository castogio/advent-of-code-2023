from __future__ import annotations
from copy import deepcopy

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

def find_symmetry_loc(m: Matrix, exlude: int = -1) -> int:
    seen = [m[0]]
    result = []
    for i, row in enumerate(m[1:], start=1):
        if seen[-1] == row:
            remainder = m[i:i+len(seen)]
            previus = m[max(0, i-len(remainder)):i]
            if remainder == list(reversed(previus)):
                result.append(len(seen))
        seen.append(row)

    if len(result) == 0:
        return -1
    
    #  need to exclude already obtained result
    # more specifically this happens if the simmetry line (with smudge)
    # is below the new line and it would be picked as the longest match
    if exlude == result[-1]:
        try:
            return result[-2]
        except:
            return -1
        
    return result[-1]

def compute_p1_result(matrices: list[Matrix]) -> int:
    total = 0
    reflection_points = [(find_symmetry_loc(m), find_symmetry_loc(transpose(m))) for m in matrices]
    for rval, cval in reflection_points:
        addition = 0
        addition += rval * 100 if rval != -1 else 0
        addition += cval if cval != -1 else 0
        total += addition
    return total

def find_symmetry_smudges(m: Matrix) -> int:
    base_loc = find_symmetry_loc(m)
    for r, row in enumerate(m):
        for c, el in enumerate(row):
            new_m = deepcopy(m)
            new_m[r][c] = '#' if el == '.' else '.'
            new_loc = find_symmetry_loc(new_m, base_loc)
            if new_loc != -1 and new_loc != base_loc:
                return new_loc
    return -1

def compute_p2_result(matrices: list[Matrix]) -> int:
    total = 0
    old_reflection_points = [(find_symmetry_loc(m), find_symmetry_loc(transpose(m))) for m in matrices]
    reflection_points = [(find_symmetry_smudges(m), find_symmetry_smudges(transpose(m))) for m in matrices]
    for old, new in zip(old_reflection_points, reflection_points):
        addition = 0
        rval, cval = new if old != new else old
        addition = rval*100 if rval != -1 else cval
        total += addition
    return total

if __name__ == '__main__':
    with open('./input.txt') as f:
        matrices = load_matrices(f.read())

    print(f'part1 total = {compute_p1_result(matrices)}') # 31956
    print(f'part2 total = {compute_p2_result(matrices)}') # 37617

