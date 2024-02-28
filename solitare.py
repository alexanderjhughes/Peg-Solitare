import board
import sys


def game():
    b = board.PegSolitaireBoard()
    b.display_board()
    while True:
        # Get the move from the user
        from_row, from_col = map(int, input(
            "Enter the row and column of the peg to move (separated by space): ").split())
        to_row, to_col = map(int, input(
            "Enter the row and column of the hole to move to (separated by space): ").split())
        # Make the move
        b.make_move(from_row, from_col, to_row, to_col)
        # Display the board
        b.display_board()
        # Check if the game is over
        # if b.is_game_over():
        #     print("Game over!")
        #     break


if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) == 0:
        game()
    else:
        if args[0] == "display":
            b = board.PegSolitaireBoard()
            b.display_board()
        elif args[0] == "game":
            game()
