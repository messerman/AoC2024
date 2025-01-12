#!/usr/bin/env python3
import cProfile
from copy import copy

from tools.grid import Grid, GridCell

PARTS = [2]#[1, 2]
FILES = ['sample.txt', 'sample1.txt', 'sample2.txt', 'sample3.txt', 'sample4.txt']#, 'input.txt']
PAUSE = False

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
                fences.add(GridCell(cell.x, cell.y - 0.5))
            s = cell.south()
            if not grid.in_bounds(s) or grid[s].value != cell.value:
                fences.add(GridCell(cell.x, cell.y + 0.5))
            e = cell.east()
            if not grid.in_bounds(e) or grid[e].value != cell.value:
                fences.add(GridCell(cell.x + 0.5, cell.y))
            w = cell.west()
            if not grid.in_bounds(w) or grid[w].value != cell.value:
                fences.add(GridCell(cell.x - 0.5, cell.y))
        area = len(group)
        perimeter = len(fences)
        total += area * perimeter
        # print(f'{area} x {perimeter} = {area * perimeter}')

    return total

# A region of R plants with price 12 * 10 = 120.        12 * 9
# A region of I plants with price 4 * 4 = 16.       OK
# A region of C plants with price 14 * 22 = 308.        14 * 19
# A region of F plants with price 10 * 12 = 120.        10 * 11
# A region of V plants with price 13 * 10 = 130.    OK
# A region of J plants with price 11 * 12 = 132.        11 * 11
# A region of C plants with price 1 * 4 = 4.        OK
# A region of E plants with price 13 * 8 = 104.     OK
# A region of I plants with price 14 * 16 = 224.        14 * 14
# A region of M plants with price 5 * 6 = 30.       OK
# A region of S plants with price 3 * 6 = 18.       OK

def find_sides(fences: set[GridCell], grid: Grid) -> set[GridCell]:
    # print('----' * 5)
    # print(fences)
    sides: set[GridCell] = set()
    visited: set[GridCell] = set()
    to_visit: set[GridCell] = copy(fences)
    while to_visit:
        fence = to_visit.pop()
        if fence in visited:
            continue
        visited.add(fence)
        # print('\t', repr(fence))

        if fence.value == '-':
            potential = list(filter(lambda f: fence.y == f.y, to_visit))
            # print('\t\t', potential)
            for f in potential:
                # print('\t\t\t', repr(f))
                delta = (f.x - fence.x) // abs(f.x - fence.x)
                # print(fence.x, f.x, fence.x+delta, f.x+delta, delta)
                for i in range(fence.x+delta, f.x+delta, delta):
                    # print('\t\t\t', i, fence.y)
                    if (i, fence.y) not in grid.cells:
                        continue
                    p = grid[(i, fence.y)]
                    if p in potential:
                        # print('\t\t\t\t', repr(p), 'yes')
                        if p in to_visit:
                            to_visit.remove(p)
        else:
            potential = list(filter(lambda f: fence.x == f.x, to_visit))
            # print('\t\t', potential)
            for f in potential:
                # print('\t\t\t', repr(f))
                delta = (f.y - fence.y) // abs(f.y - fence.y)
                # print(fence.y+delta, f.y+delta, delta)
                for i in range(fence.y+delta, f.y+delta, delta):
                    # print('\t\t\t', fence.x, i)
                    if (fence.x, i) not in grid.cells:
                        break
                    p = grid[(fence.x, i)]
                    if p in potential:
                        # print('\t\t\t\t', 'yes')
                        if p in to_visit:
                            to_visit.remove(p)

        sides.add(fence)

    # print(sides)
    # print('----' * 5)
    return sides

def solution2(my_input: list[str]) -> int:
    grid = parse(my_input)
    # print(grid)
    total = 0
    for group in grid.groups():
        # if group[0].value != 'R':
        #     continue
        # print(group)
        fences: set[GridCell] = set()
        for cell in group:
            n = cell.north()
            if not grid.in_bounds(n) or grid[n].value != cell.value:
                fence = GridCell(cell.x, cell.y - 0.5, '-')
                fences.add(fence)
                grid.cells[(fence.x, fence.y)] = fence
            s = cell.south()
            if not grid.in_bounds(s) or grid[s].value != cell.value:
                fence = GridCell(cell.x, cell.y + 0.5, '-')
                fences.add(fence)
                grid.cells[(fence.x, fence.y)] = fence
            e = cell.east()
            if not grid.in_bounds(e) or grid[e].value != cell.value:
                fence = GridCell(cell.x + 0.5, cell.y, '|')
                fences.add(fence)
                grid.cells[(fence.x, fence.y)] = fence
            w = cell.west()
            if not grid.in_bounds(w) or grid[w].value != cell.value:
                fence = GridCell(cell.x - 0.5, cell.y, '|')
                fences.add(fence)
                grid.cells[(fence.x, fence.y)] = fence
        area = len(group)
        # print(grid.cells)
        sides = fences if 1 == area else find_sides(fences, grid)
        print(group[0].value, area, len(sides), sides)
        num_sides = len(sides)
        total += area * num_sides
    return total

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
