class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return str((self.x, self.y))
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)
    
    def north(self) -> tuple[int, int]:
        return (self.x, self.y - 1)

    def south(self) -> tuple[int, int]:
        return (self.x, self.y + 1)

    def east(self) -> tuple[int, int]:
        return (self.x + 1, self.y)

    def west(self) -> tuple[int, int]:
        return (self.x - 1, self.y)
    
    def nw(self) -> tuple[int, int]:
        return (self.x - 1, self.y - 1)

    def ne(self) -> tuple[int, int]:
        return (self.x + 1, self.y - 1)

    def sw(self) -> tuple[int, int]:
        return (self.x - 1, self.y + 1)

    def se(self) -> tuple[int, int]:
        return (self.x + 1, self.y + 1)

    def neighbors(self, diagonals=False) -> list[tuple[int, int]]:
        cells = [self.north(), self.south(), self.east(), self.west()]
        if diagonals:
            cells.extend([self.nw(), self.ne(), self.sw(), self.se()])
        return cells

    def go_north(self):
        self.x, self.y = self.north()

    def go_south(self):
        self.x, self.y = self.south()

    def go_east(self):
        self.x, self.y = self.east()

    def go_west(self):
        self.x, self.y = self.west()

    def go_nw(self):
        self.x, self.y = self.nw()

    def go_ne(self):
        self.x, self.y = self.ne()

    def go_sw(self):
        self.x, self.y = self.sw()

    def go_se(self):
        self.x, self.y = self.se()
