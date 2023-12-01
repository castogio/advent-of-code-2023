from curses.ascii import isdigit


def remove_alpha_chars(line: str) -> str:
    return ''.join([ch for ch in line if ch.isdigit()])

def get_calibration_value(line: str) -> int:
    converted_line = remove_alpha_chars(line)
    return int(converted_line[0] + converted_line[-1])

def process_lines(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += get_calibration_value(line)
    return total

if __name__ == "__main__":

    with open('./day1_input.txt') as f:
        lines = f.readlines()

    total = process_lines(lines)
    print(f'total = {total}')
    