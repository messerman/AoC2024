#!/usr/bin/env python3
import cProfile
from enum import Enum

from tools.grid import Grid, GridCell

PARTS = [1]
# PARTS = [2]
# PARTS = [1, 2]
FILES = ['sample0.txt']
# FILES = ['sample0.txt', 'sample.txt']
# FILES = ['sample0.txt', 'sample.txt', 'input.txt']
# PAUSE = True
PAUSE = False

class WarehouseTypes(Enum):
    ROBOT = '@'
    WALL = '#'
    BOX = 'O'
    FLOOR = '.'

class WarehouseObject(GridCell):
    def __init__(self, x: int, y: int, value: WarehouseTypes):
        super().__init__(x, y, value.value)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(({self.x},{self.y}):{self.value})'
    
    def __str__(self) -> str:
        return self.value

class Robot(WarehouseObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WarehouseTypes('@'))

class Wall(WarehouseObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WarehouseTypes('#'))

class Box(WarehouseObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WarehouseTypes('O'))

class Direction:
    def __init__(self, direction: str):
        self.direction = direction
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.direction})'
    
    def __str__(self) -> str:
        return self.direction

def parse(my_input: list[str]) -> tuple[dict[WarehouseTypes, list[WarehouseObject]], list[Direction]]:
    result_dict: dict[WarehouseTypes, list[WarehouseObject]] = {
        WarehouseTypes.ROBOT: [],
        WarehouseTypes.WALL: [],
        WarehouseTypes.BOX: [],
        WarehouseTypes.FLOOR: []
    }
    result_list: list[Direction] = []

    grid_done = False
    for y, line in enumerate(my_input):
        try:
            if line == '':
                grid_done = True
                continue
            for x, c in enumerate(line):
                if not grid_done:
                    o: WarehouseObject
                    if c == '@':
                        o = Robot(x, y)
                    elif c == '#':
                        o = Wall(x, y)
                    elif c =='O':
                        o = Box(x, y)
                    else:
                        o = WarehouseObject(x, y, WarehouseTypes(c))
                    result_dict[WarehouseTypes(c)].append(o)
                else:
                    result_list.append(Direction(c))
        except BaseException as e:
            print(line)
            raise e
    return (result_dict, result_list)

def solution1(my_input: list[str]) -> int:
    data: tuple[dict[WarehouseTypes, list[WarehouseObject]], list[Direction]] = parse(my_input)

    warehouse: Grid = Grid.from_lists(list(data[0].values()))
    robot: Robot = data[0][WarehouseTypes.ROBOT]
    print(warehouse)

    moves = data[1]
    print(''.join(map(str, moves)))

    for move in moves:
        to_move: tuple[int, int]
        if move == '<':
            to_move = robot.west()
        elif move == '>':
            to_move = robot.east()
        elif move == '^':
            to_move = robot.north()
        else: # 'v
            to_move = robot.south()
        if warehouse.in_bounds(to_move): # TODO - account for objects and walls
            warehouse.move(robot, to_move)

    print(warehouse)

    return -1 # TODO

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
            if PAUSE:
                text = input('continue? ')
                if text:
                    break
        if PAUSE and text:
            break
