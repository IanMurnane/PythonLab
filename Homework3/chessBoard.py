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

    def set(self, x, y, color, title):
        self.board[y][x] = Figure(color, title)

    def set_ref(self, x, y, ref):
        self.board[y][x].ref = ref

    def move(self, from_x, from_y, to_x, to_y):
        figure = self.board[from_y][from_x]
        self.board[to_y][to_x] = figure
        self.board[from_y][from_x] = None

    def is_move_valid(self, from_x, from_y, to_x, to_y):
        movement = Movement()
        from_piece = self.board[from_y][from_x]
        to_piece = self.board[to_y][to_x]
        title = from_piece.get_title()
        color = from_piece.get_color()
        x_distance = to_x - from_x
        y_distance = to_y - from_y
        distance_override = 0
        can_attack = True
        can_jump = False

        # can't land on the same color piece
        if to_piece and from_piece.color == to_piece.color:
            return False

        # special rules for pawns
        if title == "PAWN":
            can_attack = False  # can't attack directly
            title += "_" + color  # movement rules are color specific
            if (from_piece.color == Color.WHITE and from_y == 6) or (from_piece.color == Color.BLACK and from_y == 1):
                distance_override = 2  # allowed 2 moves from start position

        if title == "KNIGHT":
            can_jump = True

        # check movement request is valid according to piece rules in config
        for direction in movement.directions(title):
            if self._check_direction(from_x, from_y, direction, x_distance, y_distance, distance_override, can_attack, False, can_jump):
                return True

        if movement.attack(title):
            for direction in movement.attack(title):
                if self._check_direction(from_x, from_y, direction, x_distance, y_distance, distance_override, True, True, can_jump):
                    return True

        return False

    # check if move is valid according to config rules
    def _check_direction(self, x, y, direction, x_distance, y_distance, distance_override, can_attack, must_attack, can_jump):
        test_x_distance = 0
        test_y_distance = 0
        blocking_piece = False  # found a piece along the way to a valid location
        distance = distance_override or direction[2]  # max travel distance

        for i in range(distance):
            test_x_distance += direction[0]
            test_y_distance += direction[1]
            test_x = x + test_x_distance
            test_y = y + test_y_distance

            # skip tests off the board
            if test_x < 0 or test_y < 0 or test_x > 7 or test_y > 7:
                break

            # the click area is in a valid position
            if test_x_distance == x_distance and test_y_distance == y_distance:
                # check if there was a blocking piece (and can't jump)
                if blocking_piece and not can_jump:
                    print("blocking piece")
                    return False
                # check if attacking (and is allowed to attack)
                if self.board[y + test_y_distance][x + test_x_distance] and not can_attack:
                    print("cant attack")
                    return False
                # check if attacking with nothing to attack
                if not self.board[y + test_y_distance][x + test_x_distance] and must_attack:
                    print("nothing to attack")
                    return False

                return True

            # check for blocking piece after testing for valid position, as a piece in the final position is not a block
            if self.board[y + test_y_distance][x + test_x_distance]:
                blocking_piece = True

        return False
