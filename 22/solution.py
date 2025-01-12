#!/usr/bin/env python3
import cProfile

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class SecretNumber:
    def __init__(self, num: int):
        self.num = num

    '''
    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    '''
    def evolve(self) -> 'SecretNumber':
        self.mix(self.num * 64)
        self.prune()
        self.mix(self.num // 32)
        self.prune()
        self.mix(self.num * 2048)
        self.prune()
        return self

    '''
    To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    '''
    def mix(self, num: int) -> 'SecretNumber':
        self.num ^= num
        return self

    '''
    To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    '''
    def prune(self) -> 'SecretNumber':
        self.num %= 16777216
        return self

def parse(my_input: list[str]) -> list[SecretNumber]:
    result: list[SecretNumber] = []
    for line in my_input:
        try:
            result.append(SecretNumber(int(line)))
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    result: list[int] = []
    for num in data:
        for i in range(2000):
            num.evolve()
        result.append(num.num)

    return sum(result)

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
