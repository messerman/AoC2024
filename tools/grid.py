from .position import Position

class GridCell(Position):
    def __init__(self, x: int, y: int, value: str):
        super().__init__(x, y)
        self.value = value

    def __repr__(self):
        return f'({self.x},{self.y}):{self.value}'
    
    def __str__(self):
        return self.value

class Grid:
    def __init__(self, width: int, height: int, default='.'):
        self.cells: dict[tuple[int, int], GridCell] = {}
        self.width = width
        self.height = height

    def __str__(self) -> str:
        output: list[str] = []
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                row += self.at((x, y)).value
            output.append(row)
        return'\n'.join(output)

    def at(self, pos: tuple[int, int]) -> GridCell:
        return self.cells[pos]
    
    def __getitem__(self, index: tuple[int, int]) -> GridCell:
        return self.at(index)

    def set(self, x: int, y: int, value: str) -> bool:
        if not self.in_bounds((x, y)):
            return False
        self.cells[(x, y)] = GridCell(x, y, value)
        return True

    def find(self, value: str) -> list[GridCell]:
        result: list[GridCell] = []
        for cell in self.cells.values():
            if cell.value == value:
                result.append(cell)
        return result

    def move(self, cell: GridCell, pos: tuple[int, int], leave_behind='.') -> bool:
        old_pos = cell.to_tuple()
        cell.move(pos)
        is_in_bounds = self.in_bounds(pos)
        if not is_in_bounds:
            self.cells.pop(old_pos) # remove from our cells
        self.set(old_pos[0], old_pos[1], leave_behind) # leave behind the right value

        return True


    def in_bounds(self, pos: tuple[int, int]) -> bool:
        x,y = pos
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def search_from(self, x: int, y: int, length: int, diagonals = False) -> list[str]:
        cell = self[(x,y)]
        result = []
        directions = [GridCell.north, GridCell.east, GridCell.south, GridCell.west]
        if diagonals:
            directions.extend([GridCell.nw, GridCell.ne, GridCell.sw, GridCell.se])
        for direction in directions:
            res = []
            next_cell = cell
            for i in range(length):
                res.append(next_cell.value)
                try:
                    next_cell = self.at(direction(next_cell))
                except:
                    break
            if len(res) == length:
                result.append(''.join(res))
        return result
