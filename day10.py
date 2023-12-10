from __future__ import annotations
from dataclasses import dataclass
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


@dataclass
class Location:
    x: int
    y: int

    def __add__(self, o: Location) -> Location:
        return Location(self.x+o.x, self.y+o.y)
    
    def __sub__(self, o: Location) -> Location:
        return Location(self.x-o.x, self.y-o.y)

@dataclass
class Map:
    tiles: list[list[str]]
    _start_point: Location | None = None
    _loop: list[Location] | None = None

    def get_start_point(self) -> Location:
        if self._start_point is None:
            for y, row in enumerate(self.tiles):
                for x, tile in enumerate(row):
                    if tile == 'S':
                        self._start_point = Location(x, y)
        return self._start_point
    
    def get_next_location(self, c: Location, p: Location) -> Location | None:
        cur_content = self.tiles[c.y][c.x]
        if cur_content in {'S', '.'}:
            return None
        if cur_content == '|':
            match c - p:
                case Location(0, 1): return c + Location(0, 1)
                case Location(0, -1): return c + Location(0, -1)
        elif cur_content == '-':
            match c - p:
                case Location(1, 0): return c + Location(1, 0)
                case Location(-1, 0): return c + Location(-1, 0)
        elif cur_content == 'J':
            match c - p:
                case Location(1, 0): return c + Location(0, -1)
                case Location(0, 1): return c + Location(-1, 0)
        elif cur_content == '7':
            match c - p:
                case Location(1, 0): return c + Location(0, 1)
                case Location(0, -1): return c + Location(-1, 0)
        elif cur_content == 'F':
            match c - p:
                case Location(0,-1): return c + Location(1, 0)
                case Location(-1, 0): return c + Location(0, 1)
        elif cur_content == 'L':
            match c - p:
                case Location(0,1): return c + Location(1, 0)
                case Location(-1, 0): return c + Location(0, -1)
        return None
    
    def compute_loop(self) -> list[Location]:

        if self._loop is not None:
            return self._loop


        loop = [self.get_start_point()]
        previous_loc = loop[0]

        for l in [Location(0, -1), Location(1, 0), Location(0,1), Location(-1,0)]:
            current_loc = previous_loc + l
            if next_loc := self.get_next_location(current_loc, previous_loc):
                loop.append(current_loc)
                loop.append(next_loc)
                previous_loc, current_loc = current_loc, next_loc
                break

        while True:
            next_loc = self.get_next_location(current_loc, previous_loc)
            if not next_loc or next_loc == loop[0]:
                break
            loop.append(next_loc)
            previous_loc, current_loc = current_loc, next_loc

        self._loop = loop
        return loop
    
    def purge_unused_tiles(self) -> Map:
        new_tiles = []
        loop = self.compute_loop()
        for i, r in enumerate(self.tiles):
            new_row = []
            for j in r:
                if Location(i, j) in loop:
                    new_row.append(self.tiles[i][j])
                else:
                    new_row.append('.')
            new_tiles.append(new_row)
        self.tiles = new_tiles
        return self

    def get_inside_tiles(self) -> list[Location]:
        inside_tiles = []
        poly = Polygon([Point(loc.x, loc.y) for loc in self.compute_loop()])
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                    if tile == '.':
                        loc = Location(x, y)
                        p = Point(loc.x, loc.y)
                        if poly.contains(p):
                            inside_tiles.append(loc)
        return inside_tiles

    @staticmethod
    def loads(s: list[str]) -> Map:
        return Map([list(row.strip()) for row in s])

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'part 1 len = {len(Map.loads(lines).compute_loop()) // 2}')
    print(f'part 2 tot = {len(Map.loads(lines).purge_unused_tiles().get_inside_tiles())}')


    # sample = '''FF7FSF7F7F7F7F7F---7
    #             L|LJ||||||||||||F--J
    #             FL-7LJLJ||||||LJL-77
    #             F--JF--7||LJLJ7F7FJ-
    #             L---JF-JLJ.||-FJLJJ7
    #             |F|F-JF---7F7-L7L|7|
    #             |FFJF7L7F-JF7|JL---7
    #             7-L-JL7||F7|L7F-7F7|
    #             L.L7LFJ|||||FJL7||LJ
    #             L7JLJL-JLJLJL--JLJ.L'''
    # # assert len(Map.loads(sample.splitlines()).get_inside_tiles()) == 8

    # map = Map.loads(sample.splitlines())
    # map.purge_unused_tiles()

    # inside = map.get_inside_tiles()
    # for y, row in enumerate(map.tiles):
    #     for x, v in enumerate(row):
    #         if Location(x, y) in map.compute_loop():
    #             print('x', end='')
    #         else:
    #             if Location(x, y) in inside:
    #                 print('I', end='')
    #             else:
    #                 if v == '.':
    #                     print('0', end='')
    #                 else:
    #                     print(v, end='')
    #     print()

    # print(inside)