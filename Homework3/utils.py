from enum import Enum


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Title(Enum):
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    KING = 4
    QUEEN = 5
    PAWN = 6


class WhiteIcon(Enum):
    ROOK = "\u2656"
    KNIGHT = "\u2658"
    BISHOP = "\u2657"
    KING = "\u2654"
    QUEEN = "\u2655"
    PAWN = "\u2659"


class BlackIcon(Enum):
    ROOK = "\u265C"
    KNIGHT = "\u265E"
    BISHOP = "\u265D"
    KING = "\u265B"
    QUEEN = "\u265A"
    PAWN = "\u265F"


# class DefaultRow(Enum):
#     MONARCH = [
#         Title.ROOK,
#         Title.KNIGHT,
#         Title.BISHOP,
#         Title.KING,
#         Title.QUEEN,
#         Title.BISHOP,
#         Title.KNIGHT,
#         Title.ROOK,
#     ]
#     PAWN = [Title.PAWN] * 8
#     EMPTY = [Title.EMPTY] * 8


# class Position:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
