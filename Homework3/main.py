from math import floor
from tkinter import *

from chessBoard import ChessBoard
from config import Color, Title


WIDTH = 600
HEIGHT = 600
CELL_SIZE = 60
OFFSET_X = 30
OFFSET_Y = 32
LIGHT_TILE = "#B1E4B8"
DARK_TILE = "#70A2A3"
TITLE = "ChessBoard"

chessBoard = ChessBoard()
first_click = None

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
    global first_click

    cell_x = get_click_cell(args[0].x) - 1
    cell_y = get_click_cell(args[0].y) - 1

    if not first_click:
        # a piece is required on first click
        if not chessBoard.get(cell_x, cell_y):
            return
        first_click = (cell_x, cell_y)
    else:
        from_x = first_click[0]
        from_y = first_click[1]
        to_x = cell_x
        to_y = cell_y
        move_x = (to_x - from_x) * CELL_SIZE
        move_y = (to_y - from_y) * CELL_SIZE
        first_click = None
        from_piece = chessBoard.get(from_x, from_y)
        to_piece = chessBoard.get(to_x, to_y)
        # check valid move
        if not chessBoard.is_move_valid(from_x, from_y, to_x, to_y):
            return
        # "beat" any existing piece
        if to_piece:
            canvas.delete(to_piece.ref)
        # check for pawn promotion
        if from_piece.title == Title.PAWN and (to_y == 0 or to_y == 7):
            canvas.delete(from_piece.ref)
            chessBoard.set(from_x, from_y, from_piece.color, Title.QUEEN)
            chessBoard.set_ref(from_x, from_y, canvas.create_text(
                (to_x + 1) * CELL_SIZE + OFFSET_X,
                (to_y + 1) * CELL_SIZE + OFFSET_Y,
                text=chessBoard.get(from_x, from_y),
                fill=Color(from_piece.color).name,
                font="Helvetica 48",
                tags=("handleClick", "pieces")
            ))
            chessBoard.move(from_x, from_y, to_x, to_y)
        else:
            # move piece
            canvas.move(from_piece.ref, move_x, move_y)
            chessBoard.move(from_x, from_y, to_x, to_y)
        canvas.tag_raise("pieces")  # pieces need to have a higher z-index than the board


canvas.tag_bind("handleClick", "<Button-1>", click_handler)

win.mainloop()
