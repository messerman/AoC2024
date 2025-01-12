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
        self.permeable = True
        self.stationary = True

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(({self.x},{self.y}):{self.value})'
    
    def __str__(self) -> str:
        return self.value

class Robot(WarehouseObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WarehouseTypes('@'))
        self.permeable = False
        self.stationary = False

class Wall(WarehouseObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WarehouseTypes('#'))
        self.permeable = False
        self.stationary = True

class Box(WarehouseObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WarehouseTypes('O'))
        self.permeable = False
        self.stationary = False

class Direction:
    def __init__(self, direction: str):
        self.direction = direction
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.direction})'
    
    def __str__(self) -> str:
        return self.direction

def parse(my_input: list[str]) -> tuple[Robot, dict[WarehouseTypes, list[WarehouseObject]], list[Direction]]:
    robot: Robot
    result_dict: dict[WarehouseTypes, list[WarehouseObject]] = {
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
                        roboyt = Robot(x, y)
                        continue
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

# TODO - make a generic "collision grid"
class Warehouse(Grid):
    def __init__(self, width: int, height: int, default='.'):
        # TODO - insert more things here
        super().__init__(width, height, default)

    def move(self, cell: GridCell, pos: tuple[int, int], leave_behind='.') -> bool:
        old_pos = cell.to_tuple()
        cell.move(pos)
        is_in_bounds = self.in_bounds(pos)
        # TODO - check if it will hit any obstacles
        if not is_in_bounds:
            self.cells.pop(old_pos) # remove from our cells
        self.set_cell(old_pos[0], old_pos[1], leave_behind) # leave behind the right value
        # TODO - if it hits an obstacle, attempt to move that obstacle, as well

        return True

def solution1(my_input: list[str]) -> int:
    data: tuple[Robot, dict[WarehouseTypes, list[WarehouseObject]], list[Direction]] = parse(my_input)

    robot: Robot = data[0]

    warehouse: Warehouse = Warehouse.from_lists(list(data[0].values()))
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
