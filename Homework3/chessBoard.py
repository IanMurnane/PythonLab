from figure import Figure
from utils import Color, Title


class ChessBoard:
    def __init__(self):
        # self.board = [[0] * 8] * 8
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

    # def set_figure(self, x, y, figure):
    #     self.board[x][y] = figure

    def get(self, x, y):
        return self.board[y][x]