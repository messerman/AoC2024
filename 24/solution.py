#!/usr/bin/env python3
import cProfile

PARTS = [1, 2]
FILES = ['sample.txt', 'sample1.txt', 'input.txt']
PAUSE = True

INSTRUCTIONS = {
    'AND': lambda x,y: x and y,
    'OR': lambda x,y: x or y,
    'XOR': lambda x,y: x ^ y
}

class Device:
    def __init__(self):
        self.wires: map[str, int] = {}
        self.instructions: list[tuple[str, str, str, str]] = []

    def execute(self) -> int:
        while True:
            remaining_instructions: list[tuple[str, str, str, str]] = []
            for index in range(len(self.instructions)):
                x,instruction,y,output = self.instructions[index]
                if x not in self.wires or y not in self.wires:
                    remaining_instructions.append(self.instructions[index])
                    continue
                self.wires[output] = INSTRUCTIONS[instruction](self.wires[x], self.wires[y])
                # print(self.wires)
            self.instructions = remaining_instructions
            if len(self.instructions) == 0:
                break
        result = ''.join(list(map(lambda x: str(self.wires[x]), reversed(sorted(filter(lambda x: x.startswith('z'), self.wires.keys()))))))
        # print(reversed(sorted(filter(lambda x: x.startswith('z'), self.wires.keys()))))
        # for key in sorted(self.wires.keys()):
        #     print(key, self.wires[key])
        # print(result)
        return int(result, 2)

def parse(my_input: list[str]) -> Device:
    result: Device = Device()
    wires_done = False
    for line in my_input:
        try:
            if line == '':
                wires_done = True
                continue
            if wires_done:
                parts = line.split(' ')
                result.instructions.append((parts[0], parts[1], parts[2], parts[4]))
            else:
                parts = line.split(': ')
                result.wires[parts[0]] = int(parts[1])
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    return data.execute()

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
