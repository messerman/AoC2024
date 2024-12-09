#!/usr/bin/env python3
import cProfile

PARTS = [1]#, 2]
FILES = ['sample.txt', 'input.txt']
PAUSE = True

class DiskSector:
    def __init__(self, size: int):
        self.size = size

    def __str__(self):
        return '?' * str(self.size)
    
    def __repr__(self):
        return str(self)

class DiskFile(DiskSector):
    def __init__(self, size: int, file_id: int):
        super().__init__(size)
        self.file_id = file_id

    def __str__(self):
        return str(self.file_id) * self.size
    
    def __repr__(self):
        if int(self.file_id) < 10:
            return str(self)
        return 'F' * self.size
    
class DiskBlank(DiskSector):
    def __str__(self):
        return '.' * self.size

class DiskMap:
    def __init__(self, diskmap: list[int]):
        blank = False

        file_id = 0
        block_index = 0
        self.sectors: list[DiskSector] = []
        self.blocks: dict[int, int] = {}
        for num in diskmap:
            if blank:
                self.sectors.append(DiskBlank(num))
                block_index += self.sectors[-1].size
            else:
                self.sectors.append(DiskFile(num, file_id))
                for i in range(self.sectors[-1].size):
                    self.blocks[block_index] = file_id
                    block_index += 1
                file_id += 1
            blank = not blank

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
        # for i, block in enumerate(self.blocks):
        #     result += i * (int(block) if block != '.' else 0)
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

    def defrag(self) -> None:
        i = 0
        last_file_idx = self.last_file_idx()
        while i < last_file_idx:
            # print(''.join(self.expand_blocks()))
            # print(i, last_file_idx)
            if i in self.blocks:
                i += 1
                continue
            # print(f'found a file block at {last_file_idx} - {self.blocks[last_file_idx]} - swapping with {self.blocks[i]} block at {i}')
            self.blocks[i] = self.blocks.pop(last_file_idx)
            i += 1
            last_file_idx = self.last_file_idx(last_file_idx)
        print("done")



        # blocks = list(self.blocks)

        # i = 0
        # last_file_idx = self.last_file_idx(blocks)
        # while i < last_file_idx:
        #     # print(i, blocks[i], last_file_idx, blocks[last_file_idx])
        #     block = blocks[i]
        #     if block != '.':
        #         i += 1
        #         continue
        #     blocks[i], blocks[last_file_idx] = blocks[last_file_idx], blocks[i]
        #     i += 1
        #     last_file_idx = self.last_file_idx(blocks, last_file_idx)

        #     input(''.join(blocks))

        # return ''.join(blocks)

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
    # print(diskmap)
    # print(diskmap[0], diskmap[1], diskmap[2], diskmap[3])
    # print(diskmap.expand_blocks())
    # print(''.join(diskmap.expand_blocks()))
    diskmap.defrag()
    return diskmap.checksum()

def solution2(my_input: list[str]) -> int:
    diskmap = parse(my_input)
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

