#!/usr/bin/env python3
from tools import grid

class XMasGrid(grid.Grid):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

    def is_X_MAS(self, x: int, y: int) -> bool:
        cell = self.cells[(x,y)]
        try:
            nw = self.cells[cell.nw()]
            se = self.cells[cell.se()]
            ne = self.cells[cell.ne()]
            sw = self.cells[cell.sw()]
            dr = ''.join(sorted([nw.value, se.value]))
            dl = ''.join(sorted([ne.value, sw.value]))
            return dr == 'MS' and dl == 'MS'
        except:
            return False

def parse(my_input: list[str]) -> XMasGrid:
    result = XMasGrid(len(my_input[0]), len(my_input))
    y = 0
    for line in my_input:
        try:
            line_list = list(line)
            for x in range(len(line_list)):
                result.set_cell(x, y, line_list[x])
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
    g = parse(my_input)
    found = 0
    for x in range(g.width):
        for y in range(g.height):
            if g.cells[(x,y)].value == 'A':
                found += 1 if g.is_X_MAS(x, y) else 0
    return found

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

