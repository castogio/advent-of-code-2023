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

numbers = {
    'z': {
            'zero': '0'
    },
    'o': {
            "one": '1'
    },
    't': {
            'two': '2',
            'three': '3'
    },
    'f': {
        'five': '5',
        'four': '4'
    },
    's': {
        'six': '6',
        'seven': '7'
    },
    'e': {
        'eight': '8'
    },
    'n': {
        'nine': '9'
    }
}

def _find_first_digit(line: str) -> int:
    for ch in line:
        if ch.isdigit():
            return int(ch)
    raise ValueError('no digit in line')

def _substitute_letters_to_numbers(line: str) -> str:
    converted_line = ''
    line_iter = iter(enumerate(line))
    for i, ch in line_iter:
        if ch.isdigit():
            converted_line += ch
        for k, v in numbers_chars.items():
            if line[i:].find(k) == 0:
                converted_line += v
                break
    print(converted_line)
    return converted_line

def get_calibration_value(line: str) -> int:
    converted_line = _substitute_letters_to_numbers(line)
    first_digit = _find_first_digit(converted_line)
    second_digit = _find_first_digit(converted_line[::-1])
    value = first_digit * 10 + second_digit
    print(f'str: {line} ==> {converted_line} ==> {value}')
    return value

def process_lines(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += get_calibration_value(line.strip())
    return total

if __name__ == "__main__":

    with open('assets/day1_input.txt') as f:
        lines = f.readlines()

    total = process_lines(lines)
    print(f'total = {total}')
    