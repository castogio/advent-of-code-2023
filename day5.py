from dataclasses import dataclass
from typing import Callable

Mapping = tuple[int, ...]

def parse_seeds_part1(line: str) -> list[int]:
    raw_seeds = line.split(sep=':')[1].strip().split()
    return [(int(seed_val)) for seed_val in raw_seeds]

def parse_section_entry(str_entry: str) -> Mapping:
    return tuple(int(v) for v in str_entry.split())

def get_all_mappings(lines: list[str]) -> dict[str, list[Mapping]]:

    mappings = {
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
    }
    current_list = mappings['seed-to-soil']

    it = iter(lines)
    for l in it:
        if not len(l):
            continue
        if l[0].isalpha():
            current_list = mappings[l.split()[0]]
            l = next(it)
        current_list.append(parse_section_entry(l))
    
    return mappings


def value_from_mapping(in_val: int, mappings: list[Mapping]) -> int:
    for m in mappings:
        if m[1] <= in_val < m[1]+m[2]:
            var = in_val - m[1]
            return m[0] + var
    return in_val


def parse_input(lines: list[str], parse_seed_algo: Callable) -> list[int]:
    seeds = parse_seed_algo(lines[0])

    mappings = get_all_mappings(lines[1:])

    result = []

    for s in seeds:
        soil = value_from_mapping(s, mappings['seed-to-soil'])
        fertilizer = value_from_mapping(soil, mappings['soil-to-fertilizer'])
        water = value_from_mapping(fertilizer, mappings['fertilizer-to-water'])
        light = value_from_mapping(water, mappings['water-to-light'])
        temp = value_from_mapping(light, mappings['light-to-temperature'])
        hum = value_from_mapping(temp, mappings['temperature-to-humidity'])
        result.append(value_from_mapping(hum, mappings['humidity-to-location']))

    return result


if __name__ == "__main__":

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    

    assert parse_seeds_part1('parse_seeds: 1') == [1]
    assert parse_seeds_part1('parse_seeds: 1 10') == [1, 10]

    assert parse_section_entry('50 98 0') == (50, 98, 0)
    assert parse_section_entry('50 98 1') == (50, 98, 1)
    assert parse_section_entry('50 98 2') == (50, 98, 2)

    assert value_from_mapping(79, [(50, 98, 2), (52, 50, 48)]) == 81
    assert value_from_mapping(14, [(50, 98, 2), (52, 50, 48)]) == 14
    assert value_from_mapping(55, [(50, 98, 2), (52, 50, 48)]) == 57
    assert value_from_mapping(13, [(50, 98, 2), (52, 50, 48)]) == 13

    almanac_part1 = parse_input(lines, parse_seeds_part1)

    print(f'day 1 minimum location =  {min(almanac_part1)}')




    
    
