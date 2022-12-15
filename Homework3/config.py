from enum import IntEnum, StrEnum


class Color(IntEnum):
    BLACK = 0
    WHITE = 1


class Title(IntEnum):
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    KING = 4
    QUEEN = 5
    PAWN = 6


class Icon(StrEnum):
    ROOK = "\u265C"
    KNIGHT = "\u265E"
    BISHOP = "\u265D"
    KING = "\u265B"
    QUEEN = "\u265A"
    PAWN = "\u265F"


# rules for movement
# directions - (x, y, distance)
# attack - (x, y)
class Movement:
    def __init__(self):
        self.ROOK = {
            "directions": [(0, -1, 7), (1, 0, 7), (0, 1, 7), (-1, 0, 7)],  # up right down left
        }
        self.KNIGHT = {
            "directions": [
                (-1, -2, 1), (1, -2, 1),  # up-left up-right
                (2, -1, 1), (2, 1, 1),  # right-up right-down
                (-1, 2, 1), (1, 2, 1),  # down-left down-right
                (-2, -1, 1), (-2, 1, 1),  # left-up left-down
            ],
        }
        self.BISHOP = {
            "directions": [
                (1, -1, 7),  # up-right
                (1, 1, 7),  # right-down
                (-1, 1, 7),  # down-left
                (-1, -1, 7),  # up-left
            ],
        }
        self.KING = {
            "directions": [
                (0, -1, 1),  # up
                (1, -1, 1),  # up-right
                (1, 0, 1),  # right
                (1, 1, 1),  # right-down
                (0, 1, 1),  # down
                (-1, 1, 1),  # down-left
                (-1, 0, 1),  # left
                (-1, -1, 1),  # up-left
            ],
        }
        self.QUEEN = {
            "directions": [
                (0, -1, 7),  # up
                (1, -1, 7),  # up-right
                (1, 0, 7),  # right
                (1, 1, 7),  # right-down
                (0, 1, 7),  # down
                (-1, 1, 7),  # down-left
                (-1, 0, 7),  # left
                (-1, -1, 7),  # up-left
            ],
        }
        self.PAWN_WHITE = {
            "directions": [(0, -1, 1)],  # up
            "attack": [(-1, -1, 1), (1, -1, 1)],  # up-left up-right
        }
        self.PAWN_BLACK = {
            "directions": [(0, 1, 1)],  # down
            "attack": [(-1, 1, 1), (1, 1, 1)],  # down-left down-right
        }

    def directions(self, title):
        return getattr(self, title).get("directions")

    def attack(self, title):
        return getattr(self, title).get("attack")
