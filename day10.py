from __future__ import annotations
from dataclasses import dataclass

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
    
    def get_inside_tiles(self) -> list[Location]:
        
        def is_inside(tile: Location) -> bool:

            x_hits = 0
            streak = False
            streak_count = 0
            for x in range(tile.x):
                hit = Location(x, tile.y) in self._loop
                if hit:
                    if not streak:
                        x_hits += 1
                        streak = True
                    else:
                        streak_count += 1
                else:
                    if streak and streak_count > 0:
                        x_hits += 1
                        streak_count = 0
                    streak = False
            if streak and streak_count > 0:
                x_hits += 1
                # if hit and not streak:
                #     x_hits += 1
                #     streak = True
                # if not hit:
                #     if streak:
                #         x_hits += 1
                #     streak = False


            y_hits = 0
            streak = False
            streak_count = 0
            for y in range(tile.y, len(self._loop)):
                hit = Location(tile.x, y) in self._loop
                if hit:
                    if not streak:
                        y_hits += 1
                        streak = True
                    else:
                        streak_count += 1
                else:
                    if streak and streak_count > 0:
                        y_hits += 1
                        streak_count = 0
                    streak = False
                if streak and streak_count > 0:
                    y_hits += 1
            
            legacy_hits = 0
            for y in range(tile.y, len(self._loop)):
                legacy_hits += 1 if Location(tile.x, y) in self._loop else 0

            print(x_hits)
            print(y_hits)
            print('-------')
            # assert legacy_hits == y_hits

            return x_hits % 2 and y_hits % 2
            

            # row = [l for l in loop if l.x == tile.x]
            # column = [l for l in loop if l.y == tile.y]

            # last_index = -1
            # for y in range(len(self.tiles)):
            #     if Location(tile.x, y) in self._loop:
            #         index = self._loop.index(Location(tile.x, y))
            #         if index > last_index:
            #             return False
            #         last_index = index

            # last_index = len(self.tiles[0])
            # for x in range(len(self.tiles[0])):
            #     if Location(x, tile.y) in self._loop:
            #         index = self._loop.index(Location(x, tile.y))
            #         if index < last_index:
            #             return False
            #         last_index = index
            
            # return True
            

            # x_left_count = len([l for l in loop if l.x < tile.x and l.y == tile.y])
            # x_right_count = len([l for l in loop if l.x > tile.x and l.y == tile.y])
            # y_top_count = len([l for l in loop if l.y < tile.y and l.x == tile.x])
            # y_bottom_count = len([l for l in loop if l.y > tile.y and l.x == tile.x])
            # tot_x = x_left_count + x_right_count
            # tot_y = y_top_count + y_bottom_count
            # non_border = x_left_count and x_right_count and y_top_count and y_bottom_count
            # return non_border and ((x_left_count) % 2 and (y_top_count) % 2)
        
        inside_tiles = []
        loop = self.compute_loop()
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                    if tile == '.' and is_inside(loc := Location(x, y)):
                        inside_tiles.append(loc)
        return inside_tiles

    @staticmethod
    def loads(s: list[str]) -> Map:
        return Map([list(row.strip()) for row in s])

if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'part 1 len = {len(Map.loads(lines).compute_loop()) // 2}')

    sample = '''..........
                .S------7.
                .|F----7|.
                .||....||.
                .||....||.
                .|L-7F-J|.
                .|..||..|.
                .L--JL--J.
                ..........'''
    # assert len(Map.loads(sample.splitlines()).get_inside_tiles()) == 8

    map = Map.loads(sample.splitlines())
    inside = map.get_inside_tiles()
    for y, row in enumerate(map.tiles):
        for x, v in enumerate(row):
            if Location(x, y) in map.compute_loop():
                print('x', end='')
            else:
                if Location(x, y) in inside:
                    print('I', end='')
                else:
                    if v == '.':
                        print('0', end='')
                    else:
                        print(v, end='')
        print()

    print(inside)