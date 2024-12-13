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
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Position') -> 'Position':
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> 'Position':
        return Position(other * self.x, other * self.y)

    def __rmul__(self, other: int) -> 'Position':
        return self * other

    def __lt__(self, other: 'Position') -> bool:
        origin = Position(0, 0)
        a = self - origin
        b = other - origin
        return (a.x**2 + a.y**2) < (b.x**2 + b.y**2)

    def __hash__(self) -> int:
        return hash(self.to_tuple())

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

    def move(self, pos: tuple[int, int]) -> None:
        self.x, self.y = pos

    def go_north(self):
        self.move(self.north())

    def go_south(self):
        self.move(self.south())

    def go_east(self):
        self.move(self.east())

    def go_west(self):
        self.move(self.west())

    def go_nw(self):
        self.move(self.nw())

    def go_ne(self):
        self.move(self.ne())

    def go_sw(self):
        self.move(self.sw)

    def go_se(self):
        self.move(self.se())

    def distance_to(self, other: 'Position') -> 'Position':
        return Position(other.x - self.x, other.y - self.y)
