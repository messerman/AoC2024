#!/usr/bin/env python3
from tools import grid

def parse(my_input: list[str]) -> grid.Grid:
    result = grid.Grid(len(my_input[0]), len(my_input))
    y = 0
    for line in my_input:
        try:
            line_list = list(line)
            for x in range(len(line_list)):
                result.set(x, y, line_list[x])
            y += 1
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    g = parse(my_input)
    found = 0
    for x in range(g.width):
        for y in range(g.height):
            if g.cells[(x,y)].value == 'X':
                results = g.search_from(x, y, len('XMAS'), True)
                # print(x,y,results)
                for result in results:
                    if result == 'XMAS':
                        found += 1
    return found

def solution2(my_input: list[str]) -> int:
    data = parse(my_input)
    return -1 # TODO

if __name__ == '__main__':
    for part in [1, 2]:
        print(f"---- Part { 'One' if part == 1 else 'Two' } ----")
        for file in ['sample.txt', 'input.txt']:
            print(f'-- {file} --')
            print(str(eval(f'solution{part}')(open(file, 'r').read().split('\n'))))
            text = input('continue? ')
            if text:
                break
        if text:
            break

