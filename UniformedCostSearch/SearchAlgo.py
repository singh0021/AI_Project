import time
from resource import getrusage, RUSAGE_SELF
from utility import *

class Algos:
    """
    This is an abstract class that defines the required methods to apply
    search algorithms as seen in class
    """

    def getStartState(self):
        raise NotImplementedError

    def isGoalState(self):
        raise NotImplementedError

    def getSuccessors(self):
        raise NotImplementedError

    def getCostOfAction(self):
        raise NotImplementedError

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

             
    def uniformCostSearch(self, problem):
        """
        Implements Uniform Cost Search Strategy
        """
        start_time = time.time()
        frontier = PriorityQueue()
        frontier.insert(problem.getStartState(), 0)
        frontier_set = set()
        explored = set()
        while not frontier.isEmpty():
            state = frontier.deleteMin()
            self.fringe_size -= 1
            explored.add(state)
            if problem.isGoalState(state):
                curr = state
                path = []
                while curr.prev != None:
                    path.insert(0, curr.action)
                    curr = curr.prev
                self.cost_of_path = state.cost
                self.path = path
                self.search_depth = state.depth
                self.running_time = time.time() - start_time
                return True
            
            neighbors = problem.getSuccessors(state)
            self.nodes_expanded += 1
            for neighbor in neighbors:
                neighbor.depth = state.depth + 1
                if neighbor not in explored:
                    if neighbor not in frontier_set:
                        frontier.insert(neighbor, problem.getCostOfAction(neighbor))
                        frontier_set.add(neighbor)
                        self.fringe_size += 1
                        if self.fringe_size > self.max_fringe_size:
                            self.max_fringe_size = self.fringe_size
                        if neighbor.depth > self.max_search_depth:
                            self.max_search_depth = neighbor.depth
                    else:
                        frontier.decreaseKey(neighbor, problem.getCostOfAction(neighbor))
            ram = getrusage(RUSAGE_SELF).ru_maxrss / 1024
            if ram > self.max_ram_usage:
                self.max_ram_usage = ram
        return False  
