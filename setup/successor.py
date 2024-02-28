from . import playingBoard


class PegSolitaireSuccessor:
    def __init__(self, board):
        self.board = board

    def get_valid_moves(self):
        valid_moves = []
        for row in range(7):
            for col in range(7):
                if self.board.board[row][col] == 1:  # Find a peg
                    # Check for possible moves in all four directions
                    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if self.board.is_valid_move(row, col, new_row, new_col):
                            valid_moves.append(
                                ((row, col), (new_row, new_col)))
        return valid_moves

    def generate_successors(self):
        successors = []
        for from_pos, to_pos in self.get_valid_moves():
            # Copy the current board to create a new board state
            new_board = playingBoard.PegSolitaireBoard()
            new_board.board = [row[:] for row in self.board.board]
            # Make the move on the new board
            new_board.make_move(from_pos[0], from_pos[1], to_pos[0], to_pos[1])
            successors.append(new_board)
        return successors
