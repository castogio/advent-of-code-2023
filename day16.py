from __future__ import annotations
from dataclasses import dataclass, field
from copy import copy


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, o: Position) -> Position:
        return Position(self.x+o.x, self.y+o.y)


@dataclass
class Player:
    vertical_speed: int
    horizontal_speed: int
    position: Position
    old_position: Position | None
    loop_kill: bool = False

    def move(self) -> Position:
        self.old_position = self.position
        self.position += Position(self.horizontal_speed, self.vertical_speed)
        return self.position


@dataclass
class MapLocation:
    element: str
    energized: bool = False

    def collide(self, p: Player) -> Player | None:            

        if p.old_position is None:
            raise ValueError('old player position must be set')

        match self.element:
            case '/':
                if p.old_position.x < p.position.x:
                    p.horizontal_speed = 0
                    p.vertical_speed = -1
                elif p.old_position.x > p.position.x:
                    p.horizontal_speed = 0
                    p.vertical_speed = 1
                elif p.old_position.y < p.position.y:
                    p.horizontal_speed = -1
                    p.vertical_speed = 0
                elif p.old_position.y > p.position.y:
                    p.horizontal_speed = 1
                    p.vertical_speed = 0
            case '\\':
                if p.old_position.x < p.position.x:
                    p.horizontal_speed = 0
                    p.vertical_speed = 1
                elif p.old_position.x > p.position.x:
                    p.horizontal_speed = 0
                    p.vertical_speed = -1
                elif p.old_position.y < p.position.y:
                    p.horizontal_speed = 1
                    p.vertical_speed = 0
                elif p.old_position.y > p.position.y:
                    p.horizontal_speed = -1
                    p.vertical_speed = 0
            case '|':
                if p.old_position.x != p.position.x:
                    if self.energized:
                        p.loop_kill = True
                        return None
                    p.horizontal_speed = 0
                    p.vertical_speed = 1
                    self.energized = True
                    return Player(-1,0, copy(p.position), copy(p.position))
            case '-':
                if p.old_position.y != p.position.y:
                    if self.energized:
                        p.loop_kill = True
                        return None
                    p.horizontal_speed = 1
                    p.vertical_speed = 0
                    self.energized = True
                    return Player(0,-1, copy(p.position), copy(p.position))
        
        self.energized = True
        return None
        

@dataclass
class Map:
    grid: list[list[MapLocation]]
    players: list[Player] = field(default_factory=list)

    def update(self) -> None:
        still_alive_players = []
        for p in self.players:
            new_pos = p.move()
            if not self._is_pos_within_boundaries(new_pos):
                continue
            self._visitate_location(p)
            if not p.loop_kill:
                still_alive_players.append(p)
        self.players = still_alive_players

    def play(self) -> None:
        while len(self.players):
            self.update()

    def add_player(self, p: Player) -> None:
        if not self._is_pos_within_boundaries(p.position):
            return # nothing to add
        self._visitate_location(p)
        self.players.append(p)

    def __str__(self) -> str:
        res = ''
        for row in self.grid:
            for el in row:
                res += el.element
            res += '\n'
        return res
    
    def str_energized(self) -> str:
        res = ''
        for row in self.grid:
            for el in row:
                res += '#' if el.energized else '.'
            res += '\n'
        return res
    
    def reset(self) -> None:
        self.players = []
        for row in self.grid:
            for t in row:
                t.energized = False


    def _visitate_location(self, p: Player) -> None:
        p_pos = p.position
        map_loc = self.grid[p_pos.y][p_pos.x]
        new_player = map_loc.collide(p)
        if new_player:
                self.add_player(new_player)

    def _is_pos_within_boundaries(self, pos: Position) -> bool:
        return 0 <= pos.y < len(self.grid) and 0 <= pos.x < len(self.grid[0])

    @staticmethod
    def loads(s: str) -> Map:
        grid = []
        for l in s.splitlines():
            line = []
            for slot in l.strip():
                line.append(MapLocation(slot))
            grid.append(line)
        return Map(grid)


if __name__ == '__main__':
    
    with open('./input.txt') as f:
        m: Map = Map.loads(f.read())

    p = Player(0, 1, Position(0,0), Position(-1,0))
    m.add_player(p)
    m.play()

    print(f'part 1 solution = {sum(1 for row in m.grid for t in row if t.energized)}') # 6740

    map_h = len(m.grid)
    map_w = len(m.grid[0])

    start_players = []
    for i in range(map_h):
        start_players.append(
            Player(0, 1, Position(x=0,y=i), Position(x=-1,y=i))
        )
        start_players.append(
            Player(0, -1, Position(x=map_w-1,y=i), Position(x=map_w,y=i))
        )
    for i in range(map_w):
        start_players.append(
            Player(1, 0, Position(x=i,y=0), Position(x=i,y=-1))
        )
        start_players.append(
            Player(-1, 0, Position(x=i,y=map_h-1), Position(x=i,y=map_h))
        )

    results = []
    for p in start_players:
        m.reset()
        m.add_player(p)
        m.play()
        results.append(sum(1 for row in m.grid for t in row if t.energized))

    print(f'part 2 solution = {max(results)}')

