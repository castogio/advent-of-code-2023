from curses.ascii import isdigit

numbers_chars = {
    "one": '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def substitute_letters_to_numbers(line: str) -> str:
    converted_line = ''
    for i, ch in enumerate(line):
        if ch.isalpha():
            for k, v in numbers_chars.items():
                if line[i:].find(k) == 0:
                    converted_line += v
                    break
        converted_line += ch
    return converted_line

def remove_alpha_chars(line: str) -> str:
    return ''.join([ch for ch in line if ch.isdigit()])

def get_calibration_value(line: str) -> int:
    converted_line = substitute_letters_to_numbers(line)
    converted_line = remove_alpha_chars(converted_line)
    return int(converted_line[0] + converted_line[-1])

def process_lines(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += get_calibration_value(line.strip())
    return total

if __name__ == "__main__":

    with open('day1_input.txt') as f:
        lines = f.readlines()

    total = process_lines(lines)
    print(f'total = {total}')
    