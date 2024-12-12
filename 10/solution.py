#!/usr/bin/env python3
import cProfile
from tools import grid

PARTS = [1, 2]
FILES = ['sample1.txt', 'sample2.txt', 'sample.txt', 'input.txt']
PAUSE = True

def parse(my_input: list[str]) -> grid.Grid:
    result = grid.Grid(len(my_input[0]), len(my_input))
    for y, line in enumerate(my_input):
        try:
            for x, c in enumerate(line):
                result.set_cell(x, y, c)
        except BaseException as e:
            print(line)
            raise e
    return result

def dfs(trail_map: grid.Grid, starting_cell: grid.GridCell) -> set[tuple[int, int]]:
    current = int(starting_cell.value)
    if current == 9:
        return {starting_cell.to_tuple()}
    
    result: set[tuple[int, int]] = set()
    for neighbor in starting_cell.neighbors():
        if not trail_map.in_bounds(neighbor):
            continue
        neighbor_cell = trail_map[neighbor]
        if int(neighbor_cell.value) == current + 1:
            result.update(dfs(trail_map, neighbor_cell))
    return result

def dfs2(trail_map: grid.Grid, starting_cell: grid.GridCell) -> int:
    current = int(starting_cell.value)
    if current == 9:
        return 1
    
    total = 0
    for neighbor in starting_cell.neighbors():
        if not trail_map.in_bounds(neighbor):
            continue
        neighbor_cell = trail_map[neighbor]
        if int(neighbor_cell.value) == current + 1:
            total += dfs2(trail_map, neighbor_cell)
    return total

def solution1(my_input: list[str]) -> int:
    trail_map = parse(my_input)

    scores: list[int] = []
    for trailhead in trail_map.find('0'):
        trail_destinations = dfs(trail_map, trailhead)
        scores.append(len(trail_destinations))
    return sum(scores)

def solution2(my_input: list[str]) -> int:
    trail_map = parse(my_input)

    scores: list[int] = []
    for trailhead in trail_map.find('0'):
        num_trail_destinations = dfs2(trail_map, trailhead)
        scores.append(num_trail_destinations)
    return sum(scores)

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
