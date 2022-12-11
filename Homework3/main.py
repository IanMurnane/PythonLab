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
# https://stackoverflow.com/questions/42175815/python-tkinter-canvas-when-rectangle-clicked

from tkinter import *
from chessBoard import ChessBoard
from utils import Icon
from math import floor


WIDTH = 600
HEIGHT = 600
CELL_SIZE = 60
OFFSET_X = 30
OFFSET_Y = 32
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
        x = (xIndex + 1) * CELL_SIZE
        y = (yIndex + 1) * CELL_SIZE
        color = LIGHT_TILE if (xIndex + yIndex) % 2 == 0 else DARK_TILE
        canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=color, width=0, tags="handleClick")
        # draw pieces
        piece = chessBoard.get(xIndex, yIndex)
        if piece:
            pieceColor = "white" if piece.color else "black"
            piece.ref = canvas.create_text(x + OFFSET_X, y + OFFSET_Y, text=piece, fill=pieceColor, font="Helvetica 48", tags=("handleClick", "pieces"))

canvas.pack()


def get_click_cell(i):
    cell = floor(i / CELL_SIZE)
    if cell < 1:
        cell = 1
    if cell > 8:
        cell = 8
    return cell


def click_handler(*args):
    cell_x = get_click_cell(args[0].x) - 1
    cell_y = get_click_cell(args[0].y) - 1

    canvas.move(chessBoard.get(cell_x, cell_y).ref, 0, CELL_SIZE)
    canvas.tag_raise("pieces")  # pieces need to have a higher z-index than the board


canvas.tag_bind("handleClick", "<Button-1>", click_handler)

win.mainloop()
