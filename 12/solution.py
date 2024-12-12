#!/usr/bin/env python3
import cProfile
from tools.grid import Grid, GridCell

PARTS = [1, 2]
FILES = ['sample1.txt', 'sample2.txt', 'sample.txt', 'input.txt']
PAUSE = True

def parse(my_input: list[str]) -> Grid:
    result: Grid = Grid(len(my_input[0]), len(my_input))
    try:
        for y, line in enumerate(my_input):
            for x, value in enumerate(line):
                result.set_cell(x, y, value)
    except BaseException as e:
        print(line)
        raise e

    return result

def solution1(my_input: list[str]) -> int:
    grid = parse(my_input)
    # print(grid)
    total = 0
    for group in grid.groups():
        # print(group)
        fences: set[GridCell] = set()
        for cell in group:
            n = cell.north()
            if not grid.in_bounds(n) or grid[n].value != cell.value:
                fences.add((cell.x, cell.y - 0.5))
            s = cell.south()
            if not grid.in_bounds(s) or grid[s].value != cell.value:
                fences.add((cell.x, cell.y + 0.5))
            e = cell.east()
            if not grid.in_bounds(e) or grid[e].value != cell.value:
                fences.add((cell.x + 0.5, cell.y))
            w = cell.west()
            if not grid.in_bounds(w) or grid[w].value != cell.value:
                fences.add((cell.x - 0.5, cell.y))
        area = len(group)
        perimeter = len(fences)
        total += area * perimeter
        # print(f'{area} x {perimeter} = {area * perimeter}')

    return total

def solution2(my_input: list[str]) -> int:
    grid = parse(my_input)
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
