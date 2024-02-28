from setup.goalTest import PegSolitaireGoalTest
from setup.successor import PegSolitaireSuccessor

# Node class to represent the state and path


class Node:
    def __init__(self, state, path=None):
        self.state = state
        self.path = path if path is not None else []

# Depth-first search solver, using recursion
# represents the "problem" class in the search


class DepthFirstSearchSolver:
    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.nodes_expanded = 0

    def is_goal_state(self, board):
        return PegSolitaireGoalTest(board).is_goal_state()

    def generate_successors(self, board):
        return PegSolitaireSuccessor(board).generate_successors()

    def recursive_dfs(self, node):
        # Check if current node's state is a goal state
        if self.is_goal_state(node.state):
            return node.path + [node.state]  # Return the solution path

        # Increment the number of nodes expanded
        self.nodes_expanded += 1

        # Generate successors
        successors = self.generate_successors(node.state)

        for successor in successors:
            # Create a new node for the successor with the updated path
            successor_node = Node(successor, node.path + [node.state])

            # Avoid revisiting the same state (simple loop avoidance)
            if successor not in node.path:
                # Recursive DFS call with the new node
                result = self.recursive_dfs(successor_node)
                if result:
                    return result  # Propagate the solution path up the call stack

        return None  # Goal not found in this branch

    def solve(self):
        initial_node = Node(self.initial_board)
        solution = self.recursive_dfs(initial_node)
        return solution, self.nodes_expanded
