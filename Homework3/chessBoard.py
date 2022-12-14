from figure import Figure
from config import Color, Title, Movement


class ChessBoard:
    def __init__(self):
        self.board = [
            [
                Figure(Color.BLACK, Title.ROOK),
                Figure(Color.BLACK, Title.KNIGHT),
                Figure(Color.BLACK, Title.BISHOP),
                Figure(Color.BLACK, Title.KING),
                Figure(Color.BLACK, Title.QUEEN),
                Figure(Color.BLACK, Title.BISHOP),
                Figure(Color.BLACK, Title.KNIGHT),
                Figure(Color.BLACK, Title.ROOK),
            ],
            [
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
                Figure(Color.BLACK, Title.PAWN),
            ],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
                Figure(Color.WHITE, Title.PAWN),
            ],
            [
                Figure(Color.WHITE, Title.ROOK),
                Figure(Color.WHITE, Title.KNIGHT),
                Figure(Color.WHITE, Title.BISHOP),
                Figure(Color.WHITE, Title.KING),
                Figure(Color.WHITE, Title.QUEEN),
                Figure(Color.WHITE, Title.BISHOP),
                Figure(Color.WHITE, Title.KNIGHT),
                Figure(Color.WHITE, Title.ROOK),
            ],
        ]

    def get(self, x, y):
        return self.board[y][x]

    def move(self, from_x, from_y, to_x, to_y):
        figure = self.board[from_y][from_x]
        self.board[to_y][to_x] = figure
        self.board[from_y][from_x] = None

    def is_valid(self, from_x, from_y, to_x, to_y):
        movement = Movement()
        title = Title(self.board[from_y][from_x].title).name
        x = to_x - from_x
        y = to_y - from_y
        # pawn rules are color specific
        if title == "PAWN":
            title += "_" + Color(self.board[from_y][from_x].color).name
        # is the new position valid according to the movement rules for this piece
        for direction in movement.directions(title):
            test_x = direction[0]
            test_y = direction[1]
            iterations = direction[2] or 7
            if x == test_x and y == test_y:
                return True
            for i in range(iterations - 1):  # e.g. (0, -1, 2)
                test_x += direction[0]
                test_y += direction[1]
                if x == test_x and y == test_y:
                    return True
        return False
