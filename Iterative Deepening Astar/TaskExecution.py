import timeit
import sys
from collections import deque

from heapq import heappush, heappop, heapify
import itertools

from SearchAlgo import *

goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def cal_heuristic(state):

    return sum(abs(b % board_side - g % board_side) + abs(b//board_side - g//board_side)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, board_len)))


def backtrace(current_node):
    while initial_state != current_node.state:
        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'
        moves.insert(0, movement)
        current_node = current_node.parent
    return moves

if __name__ == '__main__':
    board_len=0
    board_side=0
    moves = list()
    initial_state = list()
    if len(sys.argv) != 4:
        print('Usage: python TaskExecution.py')
        sys.exit(0)

    # Processing command line arguments
    method = sys.argv[1]
    testno = sys.argv[2]
    board =  sys.argv[3]

    data = board.split(",")
    for element in data:
        initial_state.append(int(element))
    board_len = len(initial_state)
    board_side = int(board_len ** 0.5)

    solver = Solver()
    start = timeit.default_timer()
    if method == 'ida':
        solver.ida(initial_state,goal_state, board_len, board_side, cal_heuristic)

    stop = timeit.default_timer()
    moves = backtrace(solver.goal_node)

    # Writing to output file
    resultFile = "Result_test" + testno + ".txt"
    with open(resultFile, "w") as text_file:
        text_file.write("testCase: "+board+"\n")
        text_file.write("path_to_goal: ")
        text_file.write(str(moves) + "\n")
        text_file.write("cost_of_path: ")
        text_file.write(str(len(moves)) + "\n")
        text_file.write("nodes_expanded: ")
        text_file.write(str(solver.nodes_expanded) + "\n")
        text_file.write("search_depth: ")
        text_file.write(str(solver.search_depth) + "\n")
        text_file.write("max_search_depth: ")
        text_file.write(str(solver.max_search_depth) + "\n")
        text_file.write("running_time: ")
        text_file.write(("%.8f") % (stop-start) + "\n")
        text_file.write("max_ram_usage: ")
        text_file.write(("%.8f") % solver.max_ram_usage + "\n")