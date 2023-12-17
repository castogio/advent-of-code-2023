from __future__ import annotations
from dataclasses import dataclass, field

Location = tuple[int, int]
num_inf = float('inf')

@dataclass
class Node:
    weight: float = 0
    distance: float = float('inf')
    visited: bool = False

    probe_straight: int = 1
    horiz_incidence: bool | None = None

@dataclass
class Position:
    row: int
    column: int

    def __add__(self, o: Position) -> Position:
        return Position(self.row+o.row, self.column+o.column)
    
    def __sub__(self, o: Position) -> Position:
        return Position(self.row-o.row, self.column-o.column)
    

directions: tuple[Position, ...] = (Position(-1, 0), Position(1, 0), Position(0, -1), Position(0, 1))

@dataclass
class Link:
    s: Position
    d: Position

    @property
    def is_horizonal(self) -> bool:
        return self.s.row == self.d.row



Matrix = list[list[Node]]

@dataclass
class Graph:
    m: Matrix

    def compute_shortest_paths(self) -> None:
        links = [Link(Position(0, 0), Position(1, 0)), Link(Position(0, 0), Position(0, 1))]

        while len(links):
            # print(links)
            link = min(links, key=lambda l: self.compute_link_cost(l))
            link_cost = self.compute_link_cost(link)

            dest_coord = link.d
            sour_coord = link.s


            if link_cost == num_inf:
                if sour_coord == Position(1, 3) and dest_coord == Position(1, 4):
                    print()
                links.remove(link)
                continue
            
            dest_coord = link.d
            sour_coord = link.s
            node = self.m[dest_coord.row][dest_coord.column]
            predecessor = self.m[sour_coord.row][sour_coord.column]

            if sour_coord == Position(1, 3) and dest_coord == Position(1, 4):
                print()

            if link_cost > node.distance:
                links.remove(link)
                continue

            if link_cost == node.distance:
                if node.probe_straight < predecessor.probe_straight:
                    links.remove(link)
                    continue
                # if link.is_horizonal == predecessor.horiz_incidence \
                #     and node.probe_straight < predecessor.probe_straight + 1:
                    
                # else:
                #     if node.probe_straight != 0:
                #         links.remove(link)
                #         continue




            # if node.weight == 5:
            #     print()
            node.horiz_incidence = link.is_horizonal
            node.distance = link_cost
            node.visited = True

            node.horiz_incidence = link.is_horizonal
            if node.horiz_incidence == predecessor.horiz_incidence:
                node.probe_straight = predecessor.probe_straight + 1
            else:
                node.probe_straight = 1

            for i, exp_dir in enumerate(directions):
                new_dest = link.d + exp_dir
                if new_dest != link.s and 0 <= new_dest.row < len(self.m) and 0 <= new_dest.column < len(self.m[0]):
                    if not self.m[new_dest.row][new_dest.column].visited:
                        # if dest_coord == Position(1, 3) and new_dest == Position(1, 4):
                        #     print()
                        links.append(Link(dest_coord, new_dest))

            # print(self)
            links.remove(link)

    def compute_link_cost(self, l: Link, count_streak: bool = False) -> float:
        s = self.m[l.s.row][l.s.column]
        d = self.m[l.d.row][l.d.column]

        is_straight_path = (s.horiz_incidence and l.is_horizonal) \
            or (not s.horiz_incidence and not l.is_horizonal)

        if is_straight_path and s.probe_straight+1 > 3:
            return num_inf
        
        if count_streak:
            return s.probe_straight * 100 + s.distance + d.weight
        return s.distance + d.weight
    
    def __str__(self) -> str:
        r = ''
        for row in self.m:
            for el in row:
                r += f"+{el.weight}={str(el.distance)}{'-' if el.horiz_incidence else '|'} "
            r += '\n'
        return r
        
    @staticmethod
    def load(lines: list[str]) -> Graph:
        m = []
        for row in lines:
            m.append([Node(int(el)) for el in row if len(el.strip())])
        return Graph(m)


if __name__ == '__main__':
    
    with open('./input.txt') as f:
        graph: Graph = Graph.load(f.readlines())
    
    
    m = graph.m
    m[0][0].visited = True
    m[0][0].distance = 0
    graph.compute_shortest_paths()
    
    # for row in m:
    #     for el in row:
    #         if not el.visited :
    #             print(f'error')
    
    print(m[0][0].visited)
    print(m[-1][-1])

    print(graph)

    

    # p = Player(0, 1, Position(0,0), Position(-1,0))
    # m.add_player(p)
    # m.play()

    # print(f'part 1 solution = {sum(1 for row in m.grid for t in row if t.energized)}') # 6740
        







