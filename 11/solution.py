#!/usr/bin/env python3
import cProfile

PARTS = [1]#, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = False

class Stone:
    def __init__(self, value: int):
        self.value = value
    
    def __repr__(self) -> str:
        return f'Stone({self.value})'
    
    def __str__(self) -> str:
        return str(self.value)

    def blink(self) -> list['Stone']:
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if self.value == 0:
            self.value = 1
            return [self]
        
        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        strval = str(self.value)
        strlen = len(strval)
        if strlen % 2 == 0:
            self.value = int(strval[:strlen//2])
            right = Stone(int(strval[strlen//2:]))
            return [self, right]

        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        self.value *= 2024
        return [self]

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
    data = parse(my_input)
    for i in range(25):
        # print(len(data))
        # print_stones(data)
        stones: list[Stone] = []
        for stone in data:
            stones.extend(stone.blink())
        data = stones
    # print_stones(data)
    return len(data)

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
