#!/usr/bin/env python3

class Page:
    def __init__(self, page_number: int):
        self.page_number = page_number
        self.depenencies: set[int] = set()
        self.printed = False

    def __str__(self):
        return f'{self.page_number}: {self.depenencies}'

    def __iadd__(self, other: 'Page') -> 'Page':
        self.prints_after(other.page_number)
        return self

    def prints_after(self, page_number: int) -> None:
        self.depenencies.add(page_number)

    def check_printable(self, remaining_pages: list[int]) -> list[int]:
        if self.printed:
            return []
        
        intersection = self.depenencies.intersection(set(remaining_pages))
        return list(intersection)

def parse(my_input: list[str]) -> tuple[dict[int, 'Page'], list[list[int]]]:
    pages: dict[int, Page] = {}
    map_complete = False
    to_solve: list[list[int]] = []
    for line in my_input:
        try:
            if not map_complete:
                if line.strip() == '':
                    map_complete = True
                    continue

                a,b = list(map(int, line.split('|')))
                if a not in pages:
                    pages[a] = Page(a)
                if b not in pages:
                    pages[b] = Page(b)
                pages[b] += pages[a]
            else:
                to_solve.append(list(map(int, line.split(','))))
        except BaseException as e:
            print(pages)
            print(line)
            raise e
    return (pages, to_solve)

def is_correctly_ordered(pages: dict[int, 'Page'], update: list[int]) -> bool:
    remaining = update.copy()
    while remaining:
        next_to_print = remaining.pop(0)
        if pages[next_to_print].check_printable(remaining):
            return False
    return True

def solution1(my_input: list[str]) -> int:
    data = parse(my_input)
    pages: dict[int, 'Page'] = data[0]
    updates: list[list[int]] = data[1]

    f = filter(lambda update: is_correctly_ordered(pages, update), updates)
    m = map(lambda update: update[len(update)//2], f)
    return sum(m)

def swap(l, a, b):
    l[a], l[b] = l[b], l[a]

def reorder_pages(pages: dict[int, 'Page'], update: list[int]) -> list[int]:
    ordered_update = update.copy()
    max_len = len(ordered_update) + 1
    i = 0
    while i < len(ordered_update) and not is_correctly_ordered(pages, ordered_update):
        page_num = ordered_update[i]
        needed = pages[page_num].depenencies
        swap_index = max_len
        for need in needed.intersection(set(ordered_update[i+1:])):
            idx = ordered_update.index(need)
            swap_index = min(swap_index, idx)
        if swap_index == max_len:
            i += 1
        else:
            swap(ordered_update, i, swap_index)
    return ordered_update

def solution2(my_input: list[str]) -> int:
    data = parse(my_input)
    pages: dict[int, 'Page'] = data[0]
    updates: list[list[int]] = data[1]

    f = filter(lambda update: not is_correctly_ordered(pages, update), updates)
    m = map(lambda update: reorder_pages(pages, update), f)
    return sum(map(lambda update: update[len(update)//2], m))

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
