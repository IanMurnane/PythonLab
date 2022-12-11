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


# defaultBoard = [
#         [
#             Figure(Color.BLACK, Title.ROOK),
#             Figure(Color.BLACK, Title.KNIGHT),
#             Figure(Color.BLACK, Title.BISHOP),
#             Figure(Color.BLACK, Title.KING),
#             Figure(Color.BLACK, Title.QUEEN),
#             Figure(Color.BLACK, Title.BISHOP),
#             Figure(Color.BLACK, Title.KNIGHT),
#             Figure(Color.BLACK, Title.ROOK),
#         ],
#         [Figure(Color.BLACK, Title.PAWN)] * 8,
#         [0] * 8,
#         [0] * 8,
#         [0] * 8,
#         [0] * 8,
#         [Figure(Color.WHITE, Title.PAWN)] * 8,
#         [
#             Figure(Color.WHITE, Title.ROOK),
#             Figure(Color.WHITE, Title.KNIGHT),
#             Figure(Color.WHITE, Title.BISHOP),
#             Figure(Color.WHITE, Title.KING),
#             Figure(Color.WHITE, Title.QUEEN),
#             Figure(Color.WHITE, Title.BISHOP),
#             Figure(Color.WHITE, Title.KNIGHT),
#             Figure(Color.WHITE, Title.ROOK),
#         ],
#     ]


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
