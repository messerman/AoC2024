#!/usr/bin/env python3
from tools.colors import *

def parse(my_input: list[str]) -> tuple[list[int]]:
    result1: list[int] = []
    result2: list[int] = []
    for line in my_input:
        try:
            nums = list(map(int, line.split('   ')))
            result1.append(nums[0])
            result2.append(nums[1])
        except BaseException as e:
            print(line)
            raise e
    return (result1, result2)

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    return sum(map(lambda l,r: abs(l-r), sorted(data[0]), sorted(data[1])))

def solution2(my_input: list[str]) -> int:
    data = parse(my_input)
    left, right = data
    return sum(map(lambda num: num * right.count(num), left))

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

