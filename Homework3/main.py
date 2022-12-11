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
from utils import Color, Title, Icon
from chessBoard import ChessBoard


WIDTH = 600
HEIGHT = 600
CELL = 60  # width/height in px
LIGHT_TILE = "#B1E4B8"
DARK_TILE = "#70A2A3"
TITLE = "ChessBoard"

chessBoard = ChessBoard()

# init canvas
win = Tk()
win.title(TITLE)
win.geometry("%sx%s" % (WIDTH, HEIGHT))
canvas = Canvas(win, width=WIDTH, height=HEIGHT)
# draw board
for xIndex in range(8):
    for yIndex in range(8):
        x = (xIndex + 1) * CELL
        y = (yIndex + 1) * CELL
        color = LIGHT_TILE if (xIndex + yIndex) % 2 == 0 else DARK_TILE
        canvas.create_rectangle(x, y, x + CELL, y + CELL, fill=color, width=0)
        piece = chessBoard.get(xIndex, yIndex)
        if piece:
            pieceColor = "white" if piece.color else "black"
            canvas.create_text(x + 30, y + 32, text=piece, fill=pieceColor, font="Helvetica 48")

# canvas.create_text(448, 512, text=Icon.KNIGHT.value, fill="black", font='Helvetica 48')
# canvas.tag_bind("playbutton", "<Button-1>", p)
canvas.pack()
win.mainloop()
