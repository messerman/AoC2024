#!/usr/bin/env python3
import cProfile
from itertools import chain, zip_longest

PARTS = [1, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = False

class DiskSector:
    def __init__(self, size: int):
        self.size = size
        self.kind = '?'

    def __str__(self):
        return '?' * str(self.size)
    
    def __repr__(self):
        return str(self)

class DiskFile(DiskSector):
    def __init__(self, size: int, file_id: int):
        super().__init__(size)
        self.file_id = file_id
        self.kind = 'F'

    def __str__(self):
        return str(self.file_id) * self.size
    
    def __repr__(self):
        if int(self.file_id) < 10:
            return str(self)
        return 'F' * self.size
    
class DiskBlank(DiskSector):
    def __init__(self, size: int):
        super().__init__(size)
        self.kind = 'B'

    def __str__(self):
        return '.' * self.size

class DiskMap:
    def __init__(self, diskmap: list[int]):
        blank = False

        file_id = 0
        block_index = 0
        self.sectors: list[DiskSector] = []
        self.blocks: dict[int, int] = {}
        self.blanks: list[DiskBlank] = []
        self.files: list[DiskFile] = []
        for num in diskmap:
            if blank:
                self.sectors.append(DiskBlank(num))
                self.blanks.append(self.sectors[-1])
                block_index += self.sectors[-1].size
            else:
                self.sectors.append(DiskFile(num, file_id))
                self.files.append(self.sectors[-1])
                for i in range(self.sectors[-1].size):
                    self.blocks[block_index] = file_id
                    block_index += 1
                file_id += 1
            blank = not blank
        
        # print(str(self.files))
        # print(str(self.blanks))
        # print(list(map(lambda blank: blank.size, self.blanks)))

        self.size = sum(map(lambda sector: sector.size, self.sectors))

    def __getitem__(self, index) -> str:
        if index < 0 or index > self.size:
            raise ValueError("Index is out of bounds")

        if index in self.blocks:
            return f'[{self.blocks[index]}]'
        return '.'

    def __str__(self) -> str:
        return ''.join(map(repr, self.sectors))

    def __repr__(self) -> str:
        return str(self)

    def expand_blocks(self) -> list[str]:
        return list(map(lambda index: self[index], range(self.size)))

    def checksum(self) -> int:
        # To calculate the checksum, add up the result of multiplying each of these blocks' position with the file
        # ID number it contains. The leftmost block is in position 0. If a block contains free space, skip it instead.
        result = 0
        for i, block in self.blocks.items():
            result += i * block
        return result

    def last_file_idx(self, end: int = -1) -> int:
        if end == -1:
            end = self.size

        end -= 1

        blocks = str(self)
        while True:
            if end <= 0:
                break
            if blocks[end] == '.':
                end -= 1
            else:
                break
        return end

    def reorder(self) -> None:
        i = 0
        last_file_idx = self.last_file_idx()
        while i < last_file_idx:
            if i in self.blocks:
                i += 1
                continue
            self.blocks[i] = self.blocks.pop(last_file_idx)
            i += 1
            last_file_idx = self.last_file_idx(last_file_idx)

    def flat_zip(self) -> str:
        return chain.from_iterable(zip_longest(self.files, self.blanks, fillvalue=DiskBlank(0)))

    def print_flat_zip(self) -> None:
        print(''.join(map(str, self.flat_zip())))

    def defrag(self) -> int:
        fidx = len(self.files)
        while fidx > 0:
            # print('-' * 42)
            # self.print_flat_zip()
            f = self.files[fidx - 1]
            # print('--', f.file_id, '--')
            moved = False
            bidx = 0
            while bidx < fidx:
                b = self.blanks[bidx]
                b_size = b.size
                if b.size >= f.size:
                    # print('FOUND:', bidx, f.file_id, f.size, b.size)

                    # fix front
                    self.blanks.insert(bidx+1, DiskBlank(b_size - f.size))
                    self.files.insert(bidx+1, DiskFile(f.size, f.file_id))
                    self.blanks[bidx].size = 0

                    # fix back
                    self.files.insert(fidx+1, DiskFile(0, -1))
                    self.blanks.insert(fidx+1, DiskBlank(f.size))
                    self.files[fidx].size = 0

                    moved = True
                    break
                bidx += 1
            if not moved:
                fidx -= 1
        # self.print_flat_zip()

        # TODO - should rebuild everything, instead of leaving the map broken and making a new checksum here
        
        result = 0
        # for i, block in enumerate(chain.from_iterable(zip_longest(self.files, self.blanks, fillvalue=''))):
        index = 0
        for block in self.flat_zip():
            # print(i, block)
            if isinstance(block, DiskFile) and block.file_id >= 0:
                for j in range(block.size):
                    # print(i, block.file_id)
                    result += (index+j) * block.file_id
            # print(index, block)
            index += block.size
        return result
        

def parse(my_input: list[str]) -> DiskMap:
    if len(my_input) > 1:
        raise ValueError

    result: DiskMap
    for line in my_input:
        try:
            result = DiskMap(list(map(int, list(line))))
        except BaseException as e:
            print(line)
            raise e
    return result

def solution1(my_input: list[str]) -> int:
    diskmap = parse(my_input)
    diskmap.reorder()
    return diskmap.checksum()

def solution2(my_input: list[str]) -> int:
    diskmap = parse(my_input)
    # too low - 84849197273
    # correct - 6307653242596
    return diskmap.defrag()

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

