import time
from resource import getrusage, RUSAGE_SELF
from utility import *

class Solver:
    """
    This class contains methods that use search algorithms seen in class, and computes
    some statistics about the methods given a problem.
    """
    def __init__(self):
        self.path = []
        self.cost_of_path = 0
        self.nodes_expanded = 0
        self.fringe_size = 1
        self.max_fringe_size = 1
        self.search_depth = 0
        self.max_search_depth = 0
        self.running_time = 0
        self.max_ram_usage = 0
        self.goal_node = State

    def ida(self, start_state, goal_state, board_len, board_side, h=nullHeuristic):
        start_time = time.time()
        costs=set()
        threshold = h(start_state)
        while 1:
            response = self.dls_mod(costs, start_state,goal_state, threshold, board_len, board_side,h)
            if type(response) is list:
                self.running_time = time.time() - start_time
                return response
                break
            threshold = response
            costs = set()


    def dls_mod(self, costs, start_state, goal_state, threshold, board_len, board_side,h):
        max_frontier_size=0
        explored, stack = set(), list([State(start_state, None, None, 0, 0, threshold)])

        while stack:
            node = stack.pop()
            explored.add(node.map)
            if node.state == goal_state:
                self.goal_node = node
                self.search_depth = node.depth
                return stack
            if node.key > threshold:
                costs.add(node.key)
            if node.depth < threshold:
                neighbors = reversed(self.expand(node, board_len, board_side))
                for neighbor in neighbors:
                    if neighbor.map not in explored:
                        neighbor.key = neighbor.cost + h(neighbor.state)
                        stack.append(neighbor)
                        explored.add(neighbor.map)
                        if neighbor.depth > self.max_search_depth:
                            self.max_search_depth += 1

                if len(stack) > max_frontier_size:
                    max_frontier_size = len(stack)
            ram = getrusage(RUSAGE_SELF).ru_maxrss / 1024
            if ram > self.max_ram_usage:
                self.max_ram_usage = ram
        return min(costs)

    def expand(self, node, board_len, board_side):
        # expand nodes
        self.nodes_expanded += 1
        neighbors = list()
        neighbors.append(State(self.move(node.state, 1, board_len, board_side), node, 1, node.depth + 1, node.cost + 1, 0,))
        neighbors.append(State(self.move(node.state, 2, board_len, board_side), node, 2, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 3, board_len, board_side), node, 3, node.depth + 1, node.cost + 1, 0))
        neighbors.append(State(self.move(node.state, 4, board_len, board_side), node, 4, node.depth + 1, node.cost + 1, 0))
        nodes = [neighbor for neighbor in neighbors if neighbor.state]
        return nodes

    def move(self, state, position, board_len, board_side):
        new_state = state[:]
        index = new_state.index(0)
        if position == 1:  # Up
            if index not in range(0, board_side):
                temp = new_state[index - board_side]
                new_state[index - board_side] = new_state[index]
                new_state[index] = temp
                return new_state
            else:
                return None
        if position == 2:  # Down
            if index not in range(board_len - board_side, board_len):
                temp = new_state[index + board_side]
                new_state[index + board_side] = new_state[index]
                new_state[index] = temp
                return new_state
            else:
                return None
        if position == 3:  # Left
            if index not in range(0, board_len, board_side):
                temp = new_state[index - 1]
                new_state[index - 1] = new_state[index]
                new_state[index] = temp
                return new_state
            else:
                return None
        if position == 4:  # Right
            if index not in range(board_side - 1, board_len, board_side):
                temp = new_state[index + 1]
                new_state[index + 1] = new_state[index]
                new_state[index] = temp
                return new_state
            else:
                return None
