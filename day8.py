from __future__ import annotations
from dataclasses import dataclass
from math import lcm
from typing import Generator, NamedTuple
from re import match

class Node(NamedTuple):
    name: str
    left: str
    right: str

    @staticmethod
    def loads(s: str) -> Node:
        groups = match(r"(?P<name>[A-Z]+) = \((?P<left>[A-Z]+), (?P<right>[A-Z]+)\)", s)
        if not groups:
            raise ValueError(f'not valid input --> {s}')
        return Node(**groups.groupdict())
    
    def __eq__(self, o: Node) -> bool:
        return self.name == o.name
    
    def __hash__(self) -> int:
        return hash(self.name)



@dataclass
class Map:
    steps: str
    start_point: Node
    nodes: dict[str, Node]

    def get_next_step_generator(self) -> Generator[str, None, None]:
        while True:
            for i in self.steps:
                yield i

    @staticmethod
    def loads(lines: list[str]) -> Map:
        steps = lines[0]
        nodes = {}
        start_point = None
        for l in lines[1:]:
            if not len(l):
                continue
            n = Node.loads(l.strip())
            if not start_point:
                start_point = n
            nodes[n.name] = n
        return Map(steps, start_point, nodes) # type: ignore
    
    def compute_path(self, start_point: Node | None = None, does_ends_by_z: bool = False) -> list[str]:
        path = []
        current_node = start_point if start_point else self.start_point
        step_gen = self.get_next_step_generator()

        while True:
            if does_ends_by_z and current_node.name.endswith('Z'):
                break
            if current_node.name == 'ZZZ':
                break
            step = next(step_gen)
            path.append(current_node.name)
            next_node_name = current_node.left if step == 'L' else current_node.right
            current_node = self.nodes[next_node_name]
        
        return path
    
    def get_parallel_start_nodes(self) -> list[Node]:
        return [self.nodes[sn] for sn in self.nodes if sn.endswith('A')]
    
    def get_parallel_paths_lenght(self) -> int:
        return lcm(*[len(self.compute_path(sp, does_ends_by_z=True)) for sp in self.get_parallel_start_nodes()])


if __name__ == '__main__':

    with open('./input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'part1 total = {len(Map.loads(lines).compute_path())}')
    print(f'part2 total = {Map.loads(lines).get_parallel_paths_lenght()}')