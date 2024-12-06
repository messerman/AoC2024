#!/usr/bin/env python3
from tools import grid

class Guard(grid.GridCell):
    def turn_right(self) -> None:
        self.value = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[self.value]

    def step(self, lab_map: grid.Grid) -> bool:
        direction = {'^': self.north, '>': self.east, 'v': self.south, '<': self.west}[self.value]

        success = True
        if lab_map.in_bounds(direction()):
            if lab_map.at(direction()).value == '#':
                self.turn_right()
                return False
        else:
            success = False

        lab_map.move(self, direction(), 'X')
        return success

def parse(my_input: list[str]) -> grid.Grid:
    result: grid.Grid = grid.Grid(len(my_input[0]), len(my_input))
    for y in range(len(my_input)):
        line = my_input[y]
        try:
            list(map(lambda x: result.set(x, y, line[x]), range(len(line))))
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    lab_map = parse(my_input)
    # print(lab_map)
    guard: Guard = lab_map.find('^')[0]
    guard.__class__ = Guard # TODO - there has to be a better way to do this
    
    while lab_map.in_bounds(guard.to_tuple()):
        # print(repr(guard))
        if not guard.step(lab_map):
            # print(lab_map, '\n')
            pass

    # print(repr(guard))
    # print(lab_map)

    return len(lab_map.find('X'))

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

