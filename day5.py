from __future__ import annotations
from cgitb import small
from random import seed
from typing import Generator, Iterable
from pprint import pp

from dataclasses import dataclass

Mapping = tuple[int, ...]


@dataclass
class Slice:
    base: int
    lenght: int
    seg: int


        
    
    # def subtract(self, o: Slice) -> list[Slice]:
    #     if o.base == self.base and o.head == self.head:
    #         return []
    #     if o.head < self.head:
    #         if o.base > self.base:
    #             return [Slice(self.base, o.base, self.seg), Slice(o.head, self.head, self.seg)]
    #         return [Slice(o.head, self.head, self.seg)]
    #     return [Slice(self.base, o.base, self.seg)]

def parse_seeds_part1(line: str) -> list[int]:
    raw_seeds = line.split(sep=':')[1].strip().split()
    return [(int(seed_val)) for seed_val in raw_seeds]

def chunks(lst: list[int], n) -> Generator[list[int], None, None]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def parse_seeds_part2(line: str) -> list[Slice]:
    all_pairs = [int(seed_val) for seed_val in line.split(sep=':')[1].strip().split()]
    slices = []
    for pr in chunks(all_pairs, 2):
        slices.append(Slice(pr[0], pr[1], 0))
    return slices
    

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


def parse_input_part1(lines: list[str]) -> list[int]:

    seeds = parse_seeds_part1(lines[0])

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


def reverse_value_from_mapping(in_val: int, mappings: list[Mapping]) -> int:
    for m in mappings:
        if m[0] <= in_val < m[0]+m[2]:
            var = in_val - m[0]
            return m[1] + var
    return in_val


# def find_overlaps(slice1: Iterable[Slice], slice2: Iterable[Slice]) -> list[Slice]:
#     slices = []
#     for s1 in slice1:
#         for s2 in slice2:
#             itrst = s2.intersect(s1)
#             if itrst is not None:
#                 slices.append(itrst)
#                 slices.extend(s1.subtract(itrst))
#             else:

#     return slices



def create_slice(h: tuple) -> Slice:
    return Slice(h[1], h[2], h[0]-h[1])


def map_slice(s: Slice, t: Slice) -> tuple[Slice, ...]:
    if t.base > s.base+s.lenght or t.base+t.lenght < s.base:
        return (s, )
    # if t.base == s.base and t.base+t.lenght == s.base+s.lenght:
    if t.base <= s.base and t.base+t.lenght >= s.base+s.lenght:
        return (Slice(s.base+t.seg, s.lenght, 0), )
    # if t.base > s.base and t.base+t.lenght < s.base+s.lenght:
    print(f's --> {s}')
    print(f't --> {t}')
    return (
        Slice(s.base, t.base-s.base, 0),
        Slice(t.base+t.seg, t.lenght, 0),
        Slice(t.base+t.lenght, s.lenght, 0),
    )
    # if self.base < o.base:
    #     smaller, bigger = self, o
    # else:
    #     smaller, bigger = o, self
    # if smaller.base + smaller.lenght < bigger.base:
    #     return self, 
    # else:
    #     return (Slice(smaller.base, bigger.base-smaller.base, 0), 
    #             Slice(bigger.base+bigger.seg+smaller.seg, smaller.base+smaller.lenght-bigger.base, 0),
    #             Slice(smaller.base+smaller.lenght-bigger.base, bigger.lenght-smaller.lenght, 0))

def parse_input_part2(lines: list[str]) -> int:

    seeds = parse_seeds_part2(lines[0])

    mappings = get_all_mappings(lines[1:])
    # pp(mappings)

    hum_loc_slices = tuple(create_slice(h) for h in mappings['humidity-to-location'])
    temp_hum_slices = tuple(create_slice(h) for h in mappings['temperature-to-humidity'])
    light_temp_slices = tuple(create_slice(h) for h in mappings['light-to-temperature'])
    water_light_slices = tuple(create_slice(h) for h in mappings['water-to-light'])
    fert_water_slices = tuple(create_slice(h) for h in mappings['fertilizer-to-water'])
    soil_fert_slices = tuple(create_slice(h) for h in mappings['soil-to-fertilizer'])
    seed_soil_slices = tuple(create_slice(h) for h in mappings['seed-to-soil'])

    # pp(seeds)
    # pp(seed_soil_slices)

    new_seeds = []
    for s in seeds:
        for tr in seed_soil_slices:
            new_seeds.extend(map_slice(s,tr))

    pp(new_seeds)
    
    seeds = new_seeds
    new_seeds = []
    for s in seeds:
        for tr in soil_fert_slices:
            new_seeds.extend(map_slice(s,tr))
    
    pp(new_seeds)




    
    # for sss in seed_soil_slices:
    #     for s in seeds:
    #         pp(sss.intersect(s))
    return 0


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

    almanac_part1 = parse_input_part1(lines)

    print(f'day 1 minimum location =  {min(almanac_part1)}')


    almanac_part2 = parse_input_part2(lines)

    print(f'day 2 minimum location =  {almanac_part2}')




    
    
