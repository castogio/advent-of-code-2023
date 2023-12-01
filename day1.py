from curses.ascii import isdigit


def _find_first_digit(line: str) -> int:
    for ch in line:
        if ch.isdigit():
            return int(ch)
    raise ValueError('no digit in line')

def get_calibration_value(line: str) -> int:
    first_digit = _find_first_digit(line)
    second_digit = _find_first_digit(line[::-1])
    value = first_digit * 10 + second_digit
    print(f'str: {line.strip()} ==> {value}')
    return value

def process_lines(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += get_calibration_value(line)
    return total

if __name__ == "__main__":

    with open('assets/day1_input.txt') as f:
        lines = f.readlines()

    total = process_lines(lines)
    print(f'total = {total}')
    