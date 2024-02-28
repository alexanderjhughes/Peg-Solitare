class PegSolitaireGoalTest:
    def __init__(self, board):
        self.board = board

    def is_goal_state(self):
        # This should really be a part of the board class
        # but we are keeping it separate for the sake of the assignment
        peg_count = sum(row.count(1) for row in self.board.board)
        # Check if there is exactly one peg left on the board
        return peg_count == 1
