class PegSolitaireBoard:
    def __init__(self):
        # Initialize the board with 0s for empty holes and 1s for pegs.
        # The board is represented as a 7x7 grid with -1 for invalid positions.
        self.board = [
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1]
        ]

    def display_board(self):
        for row in self.board:
            print(
                ' '.join([' ' if x == -1 else ('O' if x == 1 else '.') for x in row]))

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Check if the move is within the bounds and valid
        if from_row < 0 or from_row >= 7 or from_col < 0 or from_col >= 7 or to_row < 0 or to_row >= 7 or to_col < 0 or to_col >= 7:
            return False
        # Check if the destination is empty, the source has a peg, and the middle has a peg
        if self.board[from_row][from_col] == 1 and self.board[to_row][to_col] == 0:
            mid_row, mid_col = (
                from_row + to_row) // 2, (from_col + to_col) // 2
            return abs(from_row - to_row) == 2 and from_col == to_col and self.board[mid_row][mid_col] == 1 or \
                abs(from_col -
                    to_col) == 2 and from_row == to_row and self.board[mid_row][mid_col] == 1
        return False

    def make_move(self, from_row, from_col, to_row, to_col):
        if self.is_valid_move(from_row, from_col, to_row, to_col):
            self.board[from_row][from_col] = 0
            self.board[(from_row + to_row) // 2][(from_col + to_col) // 2] = 0
            self.board[to_row][to_col] = 1
            return True
        else:
            print("Invalid move")
            return False
