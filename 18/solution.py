#!/usr/bin/env python3
import cProfile

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

def parse(my_input: list[str]) -> list[str]:
    result: list[str] = [] # TODO - more accurate type, also for return type, above
    for line in my_input:
        try:
            result.append(line) # TODO - processing
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    return -1 # TODO

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
