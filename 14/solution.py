#!/usr/bin/env python3
import cProfile
import re

from tools.position import Position

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class Guard:
    def __init__(self, start_position: Position, velocity: Position):
        self.start_position = start_position
        self.velocity = velocity

    def __repr__(self) -> str:
        return f'Guard(start_position: {repr(self.start_position)}, velocity: {repr(self.velocity)})'

    def __str__(self) -> str:
        return f'({self.start_position}, {self.velocity})'

    def move(self, width: int, height: int, times: int) -> Position:
        p = self.start_position + (self.velocity * times)
        p.x = p.x % width
        p.y = p.y % height
        return p

def parse(my_input: list[str]) -> list[Guard]:
    result: list[Guard] = []
    for line in my_input:
        try:
            # p=0,4 v=3,-3
            m = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
            guard = Guard(Position(int(m.groups(0)[0]), int(m.groups(0)[1])), Position(int(m.groups(0)[2]), int(m.groups(0)[3])))
            result.append(guard)
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str], width: int, height: int) -> int:
    guards = parse(my_input)
    # print(list(map(str, guards)))
    # print(guards)
    quadrants = {1:[], 2:[], 3:[], 4:[]}
    for guard in guards:
        g = guard.move(width, height, 100)
        if g.x < width // 2 and g.y < height // 2:
            quadrants[1].append(g)
        elif g.x > width // 2 and g.y < height // 2:
            quadrants[2].append(g)
        elif g.x > width // 2 and g.y > height // 2:
            quadrants[3].append(g)
        elif g.x < width // 2 and g.y > height // 2:
            quadrants[4].append(g)
    # print(quadrants)
    return len(quadrants[1]) * len(quadrants[2]) * len(quadrants[3]) * len(quadrants[4])

def solution2(my_input: list[str], width: int, height: int) -> int:
    guards = parse(my_input)
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
                width = 101 if filename == 'input' else 11
                height = 103 if filename == 'input' else 7
                cProfile.run(f'result = solution{part}({lines}, {width}, {height})', f'{part}-{filename}.pstats')
                print(result)
            if PAUSE:
                text = input('continue? ')
                if text:
                    break
        if PAUSE and text:
            break
