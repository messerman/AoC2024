#!/usr/bin/env python3
import cProfile
import re

from tools.position import Position

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class Guard(Position):
    def __init__(self, start_x: int, start_y: int, velocity: Position):
        super().__init__(start_x, start_y)
        self.velocity = velocity

    def __repr__(self) -> str:
        return f'Guard(start_position: {repr(self)}, velocity: {repr(self.velocity)})'

    def __str__(self) -> str:
        return f'({self}, {self.velocity})'

    def move_steps(self, width: int, height: int, times: int) -> 'Guard':
        p = self + (self.velocity * times)
        p.x = p.x % width
        p.y = p.y % height
        return Guard(p.x, p.y, self.velocity)

def parse(my_input: list[str]) -> list[Guard]:
    result: list[Guard] = []
    for line in my_input:
        try:
            m = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
            guard = Guard(int(m.groups(0)[0]), int(m.groups(0)[1]), Position(int(m.groups(0)[2]), int(m.groups(0)[3])))
            result.append(guard)
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str], width: int, height: int) -> int:
    guards = parse(my_input)
    quadrants = {1:[], 2:[], 3:[], 4:[]}
    for guard in guards:
        g = guard.move_steps(width, height, 100)
        if g.x < width // 2 and g.y < height // 2:
            quadrants[1].append(g)
        elif g.x > width // 2 and g.y < height // 2:
            quadrants[2].append(g)
        elif g.x > width // 2 and g.y > height // 2:
            quadrants[3].append(g)
        elif g.x < width // 2 and g.y > height // 2:
            quadrants[4].append(g)
    return len(quadrants[1]) * len(quadrants[2]) * len(quadrants[3]) * len(quadrants[4])

def print_guards(guards: list[Guard], width: int, height: int) -> str:
    grid = []
    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append(0)
    for guard in guards:
        grid[guard.y][guard.x] += 1
    output = ''
    for row in grid:
        output += '\n' + ''.join(map(lambda g: str(g) if g else ' ', row))
    return output

def solution2(my_input: list[str], width: int, height: int) -> int:
    guards = parse(my_input)

    i = 0
    updated: list[Guard] = []
    print_guards(guards, width, height)
    found = False
    while not found:
        updated = []
        for guard in guards:
            updated.append(guard.move_steps(width, height, i))
        output = print_guards(updated, width, height)
        if output.count('1') == len(guards):
            print(output)
            found = True
            break
        else:
            print('.', flush=True, end='')
        i += 1

    return i

if __name__ == '__main__':
    for part in PARTS:
        print(f"---- Part {part} ----")
        for file in FILES:
            filename = file.split('.', maxsplit=1)[0]
            if part == 2 and filename != 'input':
                continue
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
