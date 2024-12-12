#!/usr/bin/env python3
import cProfile
from math import ceil, log

PARTS = [2]#[1, 2]
FILES = ['input.txt'] #['sample.txt', 'input.txt']
PAUSE = False

class Stone:
    def __init__(self, value: int):
        self.value = value
    
    def __repr__(self) -> str:
        return f'Stone({self.value})'
    
    def __str__(self) -> str:
        return str(self.value)

    CACHE: dict[(tuple[int, int]), int] = {}

    def blink(self, depth=0, maxdepth=75) -> int:
        if maxdepth < 1:
            self.CACHE[(self.value, depth)] = 1
            return self.CACHE[(self.value, depth)]

        if (self.value, depth) in self.CACHE:
            return self.CACHE[(self.value, depth)]

        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if self.value == 0:
            stone = Stone(1)
            self.CACHE[(self.value, depth)] = stone.blink(depth+1, maxdepth-1)
            return self.CACHE[(self.value, depth)]           

        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        strval = str(self.value)
        strlen = len(strval)
        if strlen % 2 == 0:
            left  = Stone(int(strval[:strlen//2]))
            right = Stone(int(strval[strlen//2:]))
            self.CACHE[(self.value, depth)] = left.blink(depth+1, maxdepth-1) + right.blink(depth+1, maxdepth-1)
            return self.CACHE[(self.value, depth)]

        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        stone = Stone(self.value * 2024)
        self.CACHE[(self.value, depth)] = stone.blink(depth+1, maxdepth-1)
        return self.CACHE[(self.value, depth)]

def parse(my_input: list[str]) -> list[Stone]:
    result: list[Stone] = []
    for line in my_input:
        try:
            for num in line.split(' '):
                result.append(Stone(int(num)))
        except BaseException as e:
            print(line)
            raise e
    return result

def print_stones(stones: list[Stone]) -> None:
    print(f'{list(map(str, stones))} - {len(stones)}')

def solution1(my_input: list[str]) -> int:
    Stone.CACHE = {}
    data = parse(my_input)
    total = 0
    for stone in data:
        length = stone.blink(0, 25)
        total += length
    return total

def solution2(my_input: list[str]) -> int:
    Stone.CACHE = {}
    data = parse(my_input)
    total = 0
    for stone in data:
        length = stone.blink(0, 75)
        total += length
    return total

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
