#!/usr/bin/env python3
import math
import re
from tools.colors import *

# in: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# out: [mul(2,4), mul(5,5), mul(11,8), mul(8,5)]
def parse(my_input: list[str]) -> list[str]:
    result: list[str] = []
    r = 'mul\(\d{1,3},\d{1,3}\)'
    for line in my_input:
        try:
            result += re.findall(r, line)
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    r = '\d+'
    total = 0
    for mul in data:
        nums = re.findall(r, mul)
        total += math.prod(map(int, nums))
    return total

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

