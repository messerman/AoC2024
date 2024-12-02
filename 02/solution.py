#!/usr/bin/env python3
from tools.colors import *

def parse(my_input: list[str]) -> list[list[int]]:
    result: list[list[int]] = []
    for line in my_input:
        try:
            result.append(list(map(int, line.split(' '))))
        except BaseException as e:
            print(line)
            raise e
    return result

def isSafe(levels: list[int]) -> bool:
    maxPositiveChange = 0
    maxNegativeChange = 0
    for i in range(len(levels) - 1):
        delta = levels[i] - levels[i+1]
        if delta == 0:
            return False
        maxNegativeChange = min(delta, maxNegativeChange)
        maxPositiveChange = max(delta, maxPositiveChange)
    # print(maxNegativeChange, maxPositiveChange)
    if not ((maxNegativeChange == 0) ^ (maxPositiveChange == 0)):
        return False
    return maxNegativeChange >= -3 and maxPositiveChange <= 3

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    return sum(map(isSafe, data))

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

