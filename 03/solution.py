#!/usr/bin/env python3
import math
import re
from tools.colors import *

def parse(my_input: list[str], pattern: str) -> list[str]:
    result: list[str] = []
    for line in my_input:
        try:
            result += re.findall(pattern, line)
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input, 'mul\(\d{1,3},\d{1,3}\)')
    total = 0
    for mul in data:
        nums = re.findall('\d+', mul)
        total += math.prod(map(int, nums))
    return total

def solution2(my_input: list[str]) -> int:
    data = parse(my_input, '(?:don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\))')
    enabled = True
    total = 0
    for command in data:
        if command == 'do()':
            enabled = True
        elif command == 'don\'t()':
            enabled = False
        elif enabled and command[:3] == 'mul':
            nums = re.findall('\d+', command)
            total += math.prod(map(int, nums))
        else:
            # print(f'ignoring ${command}')
            continue
    return total

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

