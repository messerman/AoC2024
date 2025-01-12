#!/usr/bin/env python3
import cProfile
from typing import Iterable

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
            other.connections.add(self)

class Network(set):
    def __init__(self, computers: Iterable[Computer]):
        assert(len(list(filter(lambda c: not isinstance(c, Computer), computers))) == 0)
        super().__init__(computers)
    
    def __contains__(self, o):
        if isinstance(o, str):
            return o in list(map(lambda c: c.name, self))
        return super().__contains__(o)
    
    def __repr__(self) -> str:
        return f'Network({super().__repr__(self)})'

    def __str__(self) -> str:
        computers = '\n\t'.join(list(map(str, self)))
        return f'Network:\n\t{computers}'
    
    def find_trios(self) -> 'Network["Network"]':
        result: Network[Network] = Network([])
        for c1 in self:
            for c2 in c1.connections:
                for c3 in c2.connections:
                    if c3 in c1.connections:
                        result.add(Network(Network([c1, c2, c3])))
        return result
    
    def find_chains(self, visited: 'Network', to_visit: 'Network') -> 'Network["Network"]':
        # print('-----')
        # print(visited, ',\t', to_visit)
        # print('---')

        result: Network[Network] = Network([])
        for computer in list(to_visit):
            if computer in visited:
                continue
            s = Network([computer])
            v = visited.union(s)
            # print(v)
            tv = visited.intersection(computer.connections)
            # print(tv)
            for s in self.find_chains(v, tv):
                result.add(s)
        # print('\t', result)
        # print('-----')
        return result

def parse(my_input: list[str]) -> Network:
    computers: Network = Network([])
    for line in my_input:
        try:
            a,b = line.split('-', maxsplit=1)
            A = Computer(a)
            B = Computer(b)
            A.add_connection(B)
            if A.name not in computers:
                computers.update(Network([A, B]))
        except BaseException as e:
            print(line)
            raise e
    return computers

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    print(data)
    return len(list(filter(lambda trio: trio[0].name.startswith('t') or trio[1].name.startswith('t') or trio[2].name.startswith('t'), data.find_trios())))

def solution2(my_input: list[str]) -> int:
    data = parse(my_input)
    for computer in data:
        print(data.find_chains(Network([computer]), Network(computer.connections)))
    return -1

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
