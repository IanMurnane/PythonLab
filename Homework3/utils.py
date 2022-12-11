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
