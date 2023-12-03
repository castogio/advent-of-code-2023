from dataclasses import dataclass, field
from collections import defaultdict

Line = tuple[str, ...]

@dataclass
class Number:
    str_value: str
    positions: list[tuple[int, int]] = field(default_factory=list)
    gear: tuple[int, int] = field(default_factory=tuple)

    @property
    def value(self) -> int:
        return int(self.str_value)


def get_numbers(line: Line, /, *, line_num: int) -> list[Number]:
    numbers = []
    current_number = None
    for line_pos, char in enumerate(line):
        if char.isdigit() and current_number is None:
            current_number = Number(str_value=char)
            current_number.positions.append((line_num, line_pos,))
        elif char.isdigit() and current_number is not None:
            current_number.str_value += char
            current_number.positions.append((line_num, line_pos,))
        elif not char.isdigit() and current_number is not None:
            numbers.append(current_number)
            current_number = None
    if current_number != None:
        numbers.append(current_number)
    return numbers


def are_indexes_outside_boundaries(x, y, max_x: int, max_y: int) -> bool:
    return x < 0 or y < 0 or x > max_x or y > max_y


def has_gear(number: Number, lines: list[Line]) -> bool:
    max_rows = len(lines) - 1
    max_columns = len(lines[0]) - 1
    for pos in number.positions:
        x = pos[0]
        y = pos[1]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not are_indexes_outside_boundaries(x+i, y+j, max_rows, max_columns):
                    ch = lines[x+i][y+j]
                    if ch == '*':
                        number.gear = (x+i, y+j)
                        return True
    return False


def parse_lines(lines: list[Line]) -> list[Number]:
    numbers = []
    for i, line in enumerate(lines):
        numbers.extend(get_numbers(line, line_num=i))
    return numbers

def get_total_gear_factor(numbers: list[Number]) -> int:
    total = 0
    same_gear = defaultdict(list)
    for n in numbers:
        same_gear[n.gear].append(n)

    for _, v in same_gear.items():
        if len(v) == 2:
            total += v[0].value * v[1].value

    return total

if __name__ == "__main__":

    with open('./input.txt') as f:
        lines = [tuple(line.strip()) for line in f.readlines()]

    numbers = [n for n in parse_lines(lines) if has_gear(n, lines)]
    total = get_total_gear_factor(numbers)
    
    print(f'total = {total}')