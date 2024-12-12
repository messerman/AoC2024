#!/usr/bin/env python3
import copy
import cProfile

from tools import grid

class Guard(grid.GridCell):
    def __init__(self, cell: grid.GridCell):
        super().__init__(cell.x, cell.y, cell.value)
        self.visited: dict[str, bool] = {repr(self): True}

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
        # print(self.visited)
        if repr(self) in self.visited:
            raise Exception("Loop Detected")
        self.visited[repr(self)] = True
        return success

def parse(my_input: list[str]) -> grid.Grid:
    result: grid.Grid = grid.Grid(len(my_input[0]), len(my_input))
    for y in range(len(my_input)):
        line = my_input[y]
        try:
            list(map(lambda x: result.set_cell(x, y, line[x]), range(len(line))))
        except BaseException as e:
            print(line)
            raise e
    return result

def walk(lab_map: grid.Grid) -> grid.Grid:
    guard: Guard = Guard(lab_map.find('^')[0])

    while lab_map.in_bounds(guard.to_tuple()):
        if not guard.step(lab_map):
            pass

    return lab_map


def solution1(my_input: list[str]) -> int:
    lab_map = walk(parse(my_input))
    return len(lab_map.find('X'))

def test_for_loop(lab_map: grid.Grid, new_object_pos: tuple[int, int]) -> bool:
    lab = copy.deepcopy(lab_map)
    x,y = new_object_pos
    lab.set_cell(x, y, '#')
    try:
        walk(lab)
    except:
        return True
    return False

def solution2(my_input: list[str]) -> int:
    lab_map = parse(my_input)

    guard_start: Guard = Guard(lab_map.find('^')[0]).to_tuple()
    patrol_path = walk(copy.deepcopy(lab_map))

    walked = [cell.to_tuple() for cell in patrol_path.find('X')]
    walked.pop(walked.index(guard_start)) # remove guard starting position

    total = 0
    for cell in walked:
        total += 1 if test_for_loop(lab_map, cell) else 0

    return total

if __name__ == '__main__':
    for part in [1, 2]:
        print(f"---- Part { 'One' if part == 1 else 'Two' } ----")
        for file in ['sample.txt', 'input.txt']:
            filename = file.split('.')[0]
            print(f'-- {file} --')
            with open(file, 'r') as f:
                lines = f.read().split('\n')
                result=''
                cProfile.run(f'result = solution{part}({lines})', f'{part}-{filename}.pstats')
                print(result)
            text = input('continue? ')
            if text:
                break
        if text:
            break

