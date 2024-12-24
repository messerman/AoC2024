#!/usr/bin/env python3
import cProfile

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class Computer:
    def __init__(self, name: str):
        self.name = name
        self.connections: set['Computer'] = set()

    def __repr__(self) -> str:
        return f'Computer({self.name})'

    def __str__(self) -> str:
        return f'{self.name}->{list(map(lambda c: c.name, self.connections))}'

    def __iadd__(self, other: 'Computer') -> 'Computer':
        self.add_connection(other)
        return self
    
    def __hash__(self) -> int:
        t = tuple(list(self.connections) + [self.name])
        return hash(self.name)

    def __eq__(self, other: 'Computer') -> bool:
        return self.name == other.name
    
    def __ne__(self, other: 'Computer') -> bool:
        return not (self.name == other.name)
    
    def __lt__(self, other: 'Computer') -> bool:
        return self.name < other.name

    def add_connection(self, other: 'Computer') -> None:
        if self != other:
            self.connections.add(other)
            # for c in other.connections:
            #     if c not in self.connections:
            #         self.add_connection(c) # TODO - this should just be a filter
            other.connections.add(self)

class Network:
    def __init__(self, computers: dict[str, Computer]):
        self.computers: dict[str, Computer] = computers
        # self.map_network()

    def __repr__(self) -> str:
        return f'Network({list(self.computers.keys())})'

    def __str__(self) -> str:
        computers = '\n\t'.join(list(map(str, self.computers.values())))
        return f'Network:\n\t{computers}'

    def find_reachable(self, source: Computer, visited: set[str] = set()) -> set[str]:
        visited.add(source.name)
        # if source.connections.intersection(visited):
        #     return set(list(map(lambda c: c.name, source.connections)))
        reachable: set[str] = {source.name}
        for computer in source.connections:
            print('\t', computer.name)
            if computer.name not in visited:
                reachable.add(computer.name)
                r = self.find_reachable(computer, visited)
                if source.name in r:
                    r.remove(source.name)
                reachable.update(r)
        print(f'returning {reachable} for {source.name}')
        return reachable

    def map_network(self) -> None:
        for source in list(self.computers.values()):
            print(f'--- {source} ---')
            for destination_name in self.find_reachable(source):
                destination = self.computers[destination_name]
                source.add_connection(destination)

    def find_trios(self) -> set[tuple[Computer, Computer, Computer]]:
        result: set[tuple[Computer, Computer, Computer]] = set()
        for c1 in self.computers.values():
            # print(c1.connections)
            for c2 in c1.connections:#map(lambda c: self.computers[c], c1.connections):
                for c3 in c2.connections:#map(lambda c: self.computers[c], c2.connections):
                    if c3 in c1.connections:
                        result.add(tuple(sorted([c1, c2, c3])))
        return result

def parse(my_input: list[str]) -> Network:
    computers: dict[str, Computer] = {}
    for line in my_input:
        try:
            a,b = line.split('-', maxsplit=1)
            computers[a] = computers[a] if a in computers else Computer(a)
            computers[b] = computers[b] if b in computers else Computer(b)
            computers[a].add_connection(computers[b])
            computers[b].add_connection(computers[a])
        except BaseException as e:
            print(line)
            raise e
    return Network(computers)

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    return len(list(filter(lambda trio: trio[0].name.startswith('t') or trio[1].name.startswith('t') or trio[2].name.startswith('t'), data.find_trios())))

def solution2(my_input: list[str]) -> int:
    data = parse(my_input)
    return -1 # TODO

if __name__ == '__main__':
    for part in PARTS:
        print(f"---- Part {part} ----")
        for file in FILES:
            filename = file.split('.', maxsplit=1)[0]
            print(f'-- {file} --')
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
                result: int
                cProfile.run(f'result = solution{part}({lines})', f'{part}-{filename}.pstats')
                print(result)
            if PAUSE:
                text = input('continue? ')
                if text:
                    break
        if PAUSE and text:
            break
