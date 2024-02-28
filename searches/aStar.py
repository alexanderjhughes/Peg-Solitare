from setup.playingBoard import PegSolitaireBoard
from setup.goalTest import PegSolitaireGoalTest
from setup.successor import PegSolitaireSuccessor
import heapq

# Node class to represent the state and path


class Node:
    def __init__(self, state, path=None, cost=0):
        self.state = state
        self.path = path if path is not None else []
        self.cost = cost
    # compare method

    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost


class AStarSolver:
    def __init__(self, initial_board: PegSolitaireBoard):
        self.initial_board: PegSolitaireBoard = initial_board
        self.explored: set[Node] = set()

    def heuristic(self, board: PegSolitaireBoard):
        peg_count = sum(row.count(1) for row in board.board)
        center_row = len(board.board) // 2
        center_col = len(board.board[0]) // 2
        distance_to_center = 0

        for row in range(len(board.board)):
            for col in range(len(board.board[row])):
                if board.board[row][col] == 1:  # Assuming 1 represents a peg
                    distance_to_center += abs(row -
                                              center_row) + abs(col - center_col)

        return peg_count + distance_to_center

    # A* search algorithm
    def solve(self):  # returns a solution, or failure (and the number of nodes expanded - I added this)
        # a node with state = problem.INITIAL_STATE, path = [], cost = 0
        node = Node(self.initial_board, cost=0)
        # a priority queue ordered by path cost (f(n) = g(n) + h(n)), with node as the only element
        frontier: list[tuple[int, Node]] = []
        heapq.heappush(
            frontier, (0 + self.heuristic(self.initial_board), node))

        while frontier:
            # if the frontier is empty, then return failure (and the number of nodes expanded)
            if len(frontier) == 0:
                return None, len(self.explored)
            # node = Pop(frontier) - choses the lowest-cost node in frontier
            currentCost, node = heapq.heappop(frontier)
            # if problem.GOAL_STATE(node.state) then return the solution (and the number of nodes expanded)
            if PegSolitaireGoalTest(node.state).is_goal_state():
                return node.path + [node.state], len(self.explored)

            # Add node.state to explored
            self.explored.add(self._state_to_tuple(node.state.board))

            # Get all the possible actions from the current state
            actions: list[PegSolitaireBoard] = PegSolitaireSuccessor(
                node.state).generate_successors()
            # for each action in problem.actions(node.state) do
            for successor in actions:
                successor_state_tuple = self._state_to_tuple(successor.board)
                # child = child_node(problem, node, action)
                child = Node(successor, node.path +
                             [node.state], node.cost + 1)
                # if child.state is not in explored or frontier then
                # since we are using a priority queue, we can't check if the state is in the frontier
                # we have to loop through the frontier to check if the state is in it
                if successor_state_tuple not in self.explored or not any(n.state == child.state for cost, n in frontier):
                    # frontier = insert(child, frontier)
                    heapq.heappush(
                        frontier, (child.cost + self.heuristic(child.state), child))
                    self.explored.add(successor_state_tuple)
                # else if child.state is in frontier with higher cost then
                # since we are using a priority queue, we can't check if the state is in the frontier
                elif any(n.state == child.state and n.cost > child.cost for cost, n in frontier):
                    # replace the node in the frontier with the child node
                    for i, (cost, n) in enumerate(frontier):
                        if n.state == child.state and n.cost > child.cost:
                            frontier[i] = (
                                child.cost + self.heuristic(child.state), child)
                            heapq.heapify(frontier)

    def _state_to_tuple(self, state):
        return tuple(tuple(row) for row in state)
