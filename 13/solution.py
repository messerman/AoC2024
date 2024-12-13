#!/usr/bin/env python3
import cProfile
import re

from tools.position import Position

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class ClawMachine:
    def __init__(self, button_a: Position, button_b: Position, prize: Position):
        self.a = button_a
        self.b = button_b
        self.prize = prize
        self.a_moves: dict[Position, int] = {Position(0, 0): 0}
        self.b_moves: dict[Position, int] = {Position(0, 0): 0}

        cursor = Position(0,0)
        i = 0
        while cursor.x <= self.prize.x and cursor.y <= self.prize.y:
            i += 1
            a = cursor + self.a
            self.a_moves[a] = i
            cursor.move(a.to_tuple())

        cursor.move((0,0))
        i = 0
        while cursor.x <= self.prize.x and cursor.y <= self.prize.y:
            i += 1
            b = cursor + self.b
            self.b_moves[b] = i
            cursor.move(b.to_tuple())

    def __repr__(self) -> str:
        return f'ClawMachine({self.a}, {self.b}, {self.prize})'

    def __str__(self) -> str:
        return f'A={self.a}, B={self.b}, Prize={self.prize})'

    def solutions(self) -> list[tuple[int, int]]:
        solutions: list[tuple[int, int]] = []
        for b in reversed(sorted(self.b_moves.keys())):
            needed = self.prize - b
            if needed in self.a_moves:
                solutions.append((self.a_moves[needed], self.b_moves[b]))
        return solutions

def parse(my_input: list[str]) -> list[ClawMachine]:
    result: list[ClawMachine] = []
    a: Position
    b: Position
    prize: Position
    position = 0
    for line in my_input:
        try:
            if line == '':
                position = 0
            elif position == 0 or position == 1:
                m = re.match(r'Button [A|B]: X\+(\d+), Y\+(\d+)', line)
                button = Position(int(m.groups()[0]), int(m.groups()[1]))
                if position == 0:
                    a = button
                else:
                    b = button
                position += 1
            else:
                m = re.match(r'Prize: X=(\d+), Y=(\d+)', line)
                prize = Position(int(m.groups()[0]), int(m.groups()[1]))
                result.append(ClawMachine(a, b, prize))
                position += 1
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    cost = 0
    for machine in data:
        solutions = machine.solutions()
        if not solutions:
            continue
        cost += min(map(lambda x: 3*x[0] + x[1], solutions))
    return cost

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
