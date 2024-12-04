from .position import Position

class GridCell(Position):
    def __init__(self, x: int, y: int, value: str):
        super().__init__(x, y)
        self.value = value

class Grid:
    def __init__(self, width: int, height: int):
        self.cells: dict[tuple[int, int], GridCell] = {}
        self.width = width
        self.height = height

    def __str__(self):
        output = ''
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                row += self.cells[(x, y)].value
            output += f'\n{row}'
        return output

    def set(self, x: int, y: int, value: str) -> bool:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        self.cells[(x, y)] = GridCell(x, y, value)
        return True

    def search_from(self, x: int, y: int, length: int, diagonals = False) -> list[str]:
        cell = self.cells[(x,y)]
        if cell == None:
            return None
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
                    next_cell = self.cells[direction(next_cell)]
                except:
                    break
            if len(res) == length:
                result.append(''.join(res))
        return result