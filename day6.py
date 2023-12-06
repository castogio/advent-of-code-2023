from dataclasses import dataclass
from math import ceil, floor, sqrt
from typing import Generator, Iterable

@dataclass
class WinTimes:
    min: int
    max: int

    @property
    def how_many(self) -> int:
        return self.max - self.min + 1
    
@dataclass
class Pair:
    time: int
    distance: int

    def compute_win(self) -> WinTimes:
        alpha_min = (self.time - (sqrt(self.time**2 - 4 * self.distance))) / 2
        min = ceil(alpha_min) if alpha_min != int(alpha_min) else alpha_min + 1
        alpha_max = (self.time + (sqrt(self.time**2 - 4 * self.distance))) / 2
        max = floor(alpha_max) if alpha_max != int(alpha_max) else alpha_max - 1
        return WinTimes(int(min), int(max))




def parse_input_part1(lines: list[str]) -> Generator[Pair, None, None]:
    raw_times = lines[0].split(sep=':')[1].split()
    raw_distance = lines[1].split(sep=':')[1].split()
    for t, d in zip(raw_times, raw_distance):
        yield Pair(int(t), int(d))

def parse_input_part2(lines: list[str]) -> Pair:
    t = ''.join(lines[0].split(sep=':')[1].split())
    d = ''.join(lines[1].split(sep=':')[1].split())
    return Pair(int(t), int(d))
    


def multiply(it: Iterable[int]) -> int:
    result = 1
    for i in it:
        result *= i
    return result

if __name__ == "__main__":

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    assert Pair(7, 9).compute_win() == WinTimes(2, 5)
    assert WinTimes(2, 5).how_many == 4

    assert Pair(15, 40).compute_win()  == WinTimes(4, 11)

    assert Pair(30, 200).compute_win()  == WinTimes(11, 19)

    # part 1 testdata
    # assert multiply(p.compute_win().how_many for p in parse_input(lines)) == 288

    # print(f'dat6 part 1 = {multiply(p.compute_win().how_many for p in parse_input(lines))}')

    # part 2 testdata
    assert Pair(71530, 940200).compute_win().how_many == 71503

    assert parse_input_part2(lines) == Pair(46828479, 347152214061471)

    print(f'dat6 part 2 = {parse_input_part2(lines).compute_win().how_many}')
    
