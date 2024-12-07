#!/usr/bin/env python3
import cProfile
from typing import Callable

OPERATORS: dict[str, Callable] = {
    '+': lambda x,y: x+y,
    '*': lambda x,y: x*y
}

class CalibrationEquation:
    def __init__(self, target: int, values: list[int]):
        self.target: int = target
        self.values: list[int] = values

    def solve(self) -> bool:
        # print(self.target, self.values, ':')
        if len(self.values) == 0:
            return self.target == 0
        if len(self.values) == 1:
            return self.target == self.values[0]

        # else len(self.values) >= 2:
        for op in OPERATORS.values():
            subtotal = op(self.values[0], self.values[1])
            if CalibrationEquation(self.target, [subtotal] + self.values[2:]).solve():
                # print(f'PASSED: {self.target}: {self.values}')
                return True

        # print(f'FAILED: {self.target}: {self.values}')
        return False

def parse(my_input: list[str]) -> list[CalibrationEquation]:
    result: list[CalibrationEquation] = []
    for line in my_input:
        try:
            target_str, values_str = line.split(': ')
            result.append(CalibrationEquation(int(target_str), list(map(int, values_str.split(' ')))))
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    total = sum(map(lambda equation: equation.target if equation.solve() else 0, data))        
    return total

def solution2(my_input: list[str]) -> int:
    data = parse(my_input)
    return -1 # TODO

if __name__ == '__main__':
    for part in [1, 2]:
        print(f"---- Part { 'One' if part == 1 else 'Two' } ----")
        for file in ['sample.txt', 'input.txt']:
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

