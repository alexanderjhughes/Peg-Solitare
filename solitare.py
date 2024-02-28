import sys
from setup.playingBoard import PegSolitaireBoard
from setup.goalTest import PegSolitaireGoalTest
from searches.depthFirst import DepthFirstSearchSolver


def game():
    board = PegSolitaireBoard()
    goal_test = PegSolitaireGoalTest(board)
    board.display_board()
    while True:
        # Get the move from the user
        try:
            from_row, from_col = map(int, input(
                "Enter the row and column of the peg to move (separated by space, starting from 1): ").split())
            to_row, to_col = map(int, input(
                "Enter the row and column of the hole to move to (separated by space, starting from 1): ").split())
            # Convert the 1-indexed positions to 0-indexed
            from_row -= 1
            from_col -= 1
            to_row -= 1
            to_col -= 1
            # Make the move
            board.make_move(from_row, from_col, to_row, to_col)
            # Display the board
            board.display_board()
            # Check if the game is over
            if board.is_game_over():
                print("Game over!")
                break
            # Check if the goal state is reached
            if goal_test.is_goal_state():
                print("You won!")
                break
        except ValueError:
            print("Invalid input")
        except IndexError:
            print("Invalid input")
        except KeyboardInterrupt:
            print("\nGame ended by user")
            break


def dfs():
    initial_board = PegSolitaireBoard()
    solver = DepthFirstSearchSolver(initial_board)
    solution_path, nodes_expanded = solver.solve()

    if solution_path:
        print("Solution found!")
        for step, board in enumerate(solution_path):
            print(f"Step {step}:")
            board.display_board()
        print(f"Total steps: {len(solution_path) - 1}")
        print(f"Nodes expanded: {nodes_expanded}")
        print("Goal state reached!" if PegSolitaireGoalTest(
            solution_path[-1]).is_goal_state() else "No goal state reached.")
    else:
        print("No solution found.")


if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) == 0:
        game()
    else:
        if args[0] == "display":
            board = PegSolitaireBoard()
            board.display_board()
        elif args[0] == "game":
            game()
        elif args[0] == "dfs":
            dfs()
