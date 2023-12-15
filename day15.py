from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass

def hash_algorithm(to_hash: str) -> int:
    current_value = 0
    for ch in to_hash:
        current_value += ord(ch) # increase by ASCII val
        current_value *= 17
        current_value %= 256 # reminder
    return current_value

@dataclass
class Lens:
    label: str
    focal_length: int

    def __hash__(self) -> int:
        return hash_algorithm(self.label)


class Command:

    def __init__(self, str_command: str) -> None:
        self.chars = str_command
        label, self.operator, focal_length = self._parse_str_command(str_command)
        self.lens = Lens(label, focal_length)

    def __hash__(self) -> int:
        return hash_algorithm(self.chars)
    
    def _parse_str_command(self, to_split: str) -> tuple[str, str, int]:
        label = ''
        op = ''
        num = -1
        for i, ch in enumerate(to_split):
            if ch.isalpha():
                label += ch
            if ch in {'=', '-'}:
                op += ch
            if ch.isnumeric():
                num = int(to_split[i:])
        return label, op, num
            

class HashMap:

    def __init__(self) -> None:
        self.boxes = defaultdict(list)

    def add(self, command: Command) -> None:
        lens = command.lens
        key = hash(lens)
        box = self.boxes[key]
        if command.operator == '-':
            self.boxes[key] = [l for l in box if l.label != lens.label]
        elif command.operator == '=':
            found = False
            for i, l in enumerate(box):
                if l.label == lens.label:
                    box[i] = lens
                    found = True
                    break
            if not found:
                box.append(lens)


    def get_focusing_pwr(self) -> int:
        total = 0
        for box_id, box in self.boxes.items():
            for slot, lens in enumerate(box, start=1):
                total += (box_id+1) * slot * lens.focal_length
        return total

    
if __name__ == '__main__':
    
    with open('./input.txt') as f:
        commands: list[Command] = [Command(st) for st in f.read().split(',')]

    total = 0
    for st in commands:
        total += hash(st)
    
    print(f'part1 total = {total}') # 509152

    map = HashMap()
    for c in commands:
        map.add(c)

    print(f'part2 total = {map.get_focusing_pwr()}') # 244403