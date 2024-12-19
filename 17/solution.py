#!/usr/bin/env python3
import cProfile

PARTS = [2]#[1, 2]
FILES = ['input.txt']#['sample.txt', 'sample1.txt', 'input.txt']
PAUSE = False#True

class Computer3Bit:
    def __init__(self):
        self.A: int = 0
        self.B: int = 0
        self.C: int = 0
        self.program: list[int] = []

    def __repr__(self) -> str:
        s = str(self).replace('\n', ', ')
        return f'Computer3Bit{s}'

    def __str__(self) -> str:
        return f'(A={self.A}, B={self.B}, C={self.C})\nProgram={",".join(map(str, self.program))}'

    def combo(self, num: int) -> int:
        # Combo operands 0 through 3 represent literal values 0 through 3.
        if num >= 0 and num <= 3:
            return num
    
        # Combo operand 4 represents the value of register A.
        if num == 4:
            return self.A
        
        # Combo operand 5 represents the value of register B.
        if num == 5:
            return self.B

        # Combo operand 6 represents the value of register C.
        if num == 6:
            return self.C

        # Combo operand 7 is reserved and will not appear in valid programs.
        raise(ValueError)

    # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
    def adv(self, num: int) -> None:
        self.A = self.A // 2**self.combo(num)

    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    def bxl(self, num: int) -> None:
        self.B = self.B ^ num

    #The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def bst(self, num: int) -> None:
        self.B = self.combo(num) % 8

    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, num: int) -> int:
        if self.A == 0:
            return -1
        return num

    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self, num: int) -> None:
        self.B = self.B ^ self.C

    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    def out(self, num: int) -> int:
        return self.combo(num) % 8

    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, num: int) -> None:
        self.B = self.A // 2**self.combo(num)

    # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
    def cdv(self, num: int) -> None:
        self.C = self.A // 2**self.combo(num)

    def execute(self) -> str:
        output: list[int] = []
        functions = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}

        i = 0
        while i < len(self.program) - 1:
            # print(f'({self.A}, {self.B}, {self.C}) - {i}')
            instruction = functions[self.program[i]]
            param = self.program[i+1]
            if instruction == self.out:
                output.append(instruction(param))
            elif instruction == self.jnz:
                jumpto = instruction(param)
                if jumpto != -1:
                    i = jumpto
                    continue
            else:
                instruction(param)
            i += 2
        return ','.join(map(str, output))

def parse(my_input: list[str]) -> Computer3Bit:
    result = Computer3Bit()
    for line in my_input:
        try:
            if line.startswith('Register'):
                (r, register, value) = line.split(' ')
                if register[:-1] == 'A':
                    result.A = int(value)
                elif register[:-1] == 'B':
                    result.B = int(value)
                elif register[:-1] == 'C':
                    result.C = int(value)
            elif line.startswith('Program'):
                (p, program) = line.split(' ')
                result.program = list(map(int, program.split(',')))

        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> str:
    computer = parse(my_input)
    return computer.execute()

def solution2(my_input: list[str]) -> int:
    computer = parse(my_input)
    # bst(4) // B = A % 8
    # bxl(2) // B = B^2
    # cdv(5) // C = A // 5
    # bxl(7) // B = B^7
    # bxc(4) // B = B^C
    # adv(3) // A = A // 3
    # out(5) // print(B % 8)
    # jnz(0) // jump to 0 if A != 0 else halt

    # 2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0

    #### 0:
    # B = A % 8
    # B = B^2
    # C = A // 5 (A = 5x or 10x)
    # B = B^7 (???)
    # B = B^C (B must end up evenly divisible by 8, )
    # A < 3
    # B % 8 == 0 (B evenly divisible by 8)
    # A == 0
    ###

    computer.program = computer.program[:-2]
    # computer.A = 177313
    # print(computer.execute())
    # return -1

    prev_a = [0]
    for a in [0,3,5,5,3,0,4,4,7,1,5,7,2,1,4,2]:
        As = []
        for prev in prev_a:
            print(f'looking for: out={a}, A={prev}')
            # while True:
            for i in range(7*prev, 10*(prev+1)):
                computer.A = i
                computer.B = 0
                computer.C = 0
                ans = computer.execute()
                # print(f'(looking for ({a}, {prev_a})), A={i}: out={ans}, A={computer.A}')
                if int(ans) == a and computer.A == prev:
                    print(f'A={i}: out={ans}, A={computer.A}')
                    if i == 2770 and ans == '5':
                        continue
                    # if i == 22187 and ans == '3': # this one seems ok
                    #     continue
                    # if i == 90881971 and ans == '7':
                    #     continue

                    As.append(i)
                # break
            # i += 1
        print(As)
        prev_a = As

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
