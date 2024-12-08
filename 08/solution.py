#!/usr/bin/env python3
import cProfile

from tools.position import Position
from tools.grid import Grid, GridCell

PARTS = [1, 2]
FILES = ['sample1.txt', 'sample2.txt', 'sample.txt', 'input.txt']

def parse(my_input: list[str]) -> Grid:
    result: Grid = Grid(len(my_input[0]), len(my_input))
    for y in range(len(my_input)):
        try:
            line = my_input[y]
            for x in range(len(line)):
                result.set(x, y, line[x])
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)

    antennas: dict[str, list[GridCell]] = {}
    for antenna in filter(lambda cell: cell.value != '.' , data.cells.values()):
        if antenna.value not in antennas:
            antennas[antenna.value] = []
        antennas[antenna.value].append(antenna)

    frequencies = list(antennas.keys())
    antinodes: set[tuple[int, int]] = set()
    for frequency in frequencies:
        for i in range(len(antennas[frequency]) - 1):
            for j in range(i+1 ,len(antennas[frequency])):
                a1 = antennas[frequency][i]
                a2 = antennas[frequency][j]
                l = 2 * a1 - a2
                r = 2 * a2 - a1
                if 2*(l - a1) == (l - a2) and data.in_bounds(l.to_tuple()):
                    antinodes.add(l.to_tuple())
                if 2*(r - a2) == (r - a1) and data.in_bounds(r.to_tuple()):
                    antinodes.add(r.to_tuple())

    return len(antinodes)

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
            text = input('continue? ')
            if text:
                break
        if text:
            break

