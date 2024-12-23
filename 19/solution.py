#!/usr/bin/env python3
import cProfile

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class Towel:
    def __init__(self, stripes: str):
        self.stripes = stripes

    def __str__(self) -> str:
        return self.stripes

    def __repr__(self) -> str:
        return f'Towel({self.stripes})'

class Pattern:
    def __init__(self, stripes: str, towels: list[Towel]):
        self.stripes = stripes
        self.towels = towels

    def __str__(self) -> str:
        return self.stripes

    def __repr__(self) -> str:
        return f'Pattern({self.stripes})'
    
    def find_towel_order(self, idx=0) -> bool:
        print(self, idx, self.stripes[idx:])
        if idx >= len(self.stripes):
            return True

        stripes = self.stripes[idx:]
        for towel in self.towels:
            # print('.', flush=True, end='')
            if stripes.startswith(towel.stripes):
                if self.find_towel_order(idx + len(towel.stripes)):
                    return True
        
        return False

def parse(my_input: list[str]) -> tuple[list[Towel], list[Pattern]]:
    towels: list[Towel] = []
    patterns: list[Pattern] = []
    towels_done = False
    for line in my_input:
        try:
            if not towels_done:
                if line == '':
                    towels_done = True
                    continue
                for t in line.split(', '):
                    towels.append(Towel(t))
            else:
                patterns.append(Pattern(line, towels))
        except BaseException as e:
            print(line)
            raise e
    return (towels, patterns)

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    count = 0
    for pattern in data[1]:
        print(pattern)
        if pattern.find_towel_order():
            count += 1
        # print('\n')
    return count

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
