# The Chess game should be created. To get know more about game Chess
# You should create 9 classes:
# class ChessBoard
# class Position
# class ChessFigure - which contains main attributes as color, title,
# position of the ChestBoard and method move() for one position.
# Classes derived from Chess Figure: Rook, Knight, Bishop, Queen, King and Pawn.
# Each class should have its own method move() and beat().
# For the King should be additional attributes for saving if castling
# were done and what side of the board it is located.
# Each class should be tested in the solution.

# https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode
# https://chessdelights.com/wp-content/uploads/2019/09/chesspositions2.png

from tkinter import *
from pprint import pprint
from figure import Figure
from utils import Color, Title, WhiteIcon, BlackIcon


WIDTH = 600
HEIGHT = 600
CELL = 60

win = Tk()
win.title("ChessBoard")
win.geometry("%sx%s" % (WIDTH, HEIGHT))
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
for x in range(8):
    for y in range(8):
        xx = (x + 1) * CELL
        yy = (y + 1) * CELL
        color = "#B1E4B8" if (x + y) % 2 == 0 else "#70A2A3"
        canvas.create_rectangle(xx, yy, xx + CELL, yy + CELL, fill=color, width=0, tags="playbutton")
canvas.create_text(510, 512, text=BlackIcon.QUEEN.value, fill="white", font='Helvetica 48')
canvas.create_text(448, 512, text=BlackIcon.KNIGHT.value, fill="black", font='Helvetica 48')
# canvas.tag_bind("playbutton", "<Button-1>", p)
canvas.pack()
# button = Button(canvas, text="Click Me", command=None)
# button.pack(pady=20)
win.mainloop()


class ChessBoard:
    def __init__(self):
        board = [
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
            [Figure(Color.BLACK, Title.PAWN)] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [0] * 8,
            [Figure(Color.WHITE, Title.PAWN)] * 8,
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
        # board = [[0]*8]*8

        # print(Figure(Color.WHITE, Title.KNIGHT))

        # pprint(board)

        # for x in range(8):
        #     for y in range(8):
        #         print(board[x][y])


# chessBoard = ChessBoard()
