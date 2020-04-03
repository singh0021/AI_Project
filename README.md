# N-Puzzle (AI Project)

In this assignment we shall be creating an agent to solve the 8-puzzle game. For reference purpose, we can visit [N-puzzle] for a refresher of the rules of the game. We shall be implementing 3-4 algorithms such as A Star, Uniformed Cost, Iterative Deepening Astar, and Iterative Deepening algorithms. Each one of us from group will be working on one of the algorithms and will be publishing resulst in respective folders. Description of puzzle problem is given below. At last, we shall be producing statistics about each algorithm.

Problem: An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this project, we shall represent the blank space with the number 0 and focus on the m = 3 case (8-puzzle).

Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, …, m^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.

The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.


## Tech Stack
Technologies used in this simulation,

* Python 2.7- For the implementation. For calculation of memory usage, a package has been used which makes use of linux environment.

And project is present in a [public repository][repo] on GitHub.

### Installation

This project requires Python2.7 to run.

Install Python3 and required pip packages.
To run it on Windows comment out the lines using "resource" package.
## Code Structure
There are 3 directories each having the implementation of a particular algorithm and results of few test cases that we have executed. Along with that there is a readme file in each directory to guide you how to run the code from command line.

Each directory has 3 files:
##### SearchAlgo.py - This file contains the implementation of the search algorithm.
##### TaskExecution.py - This file contains the generi code for the problem and is the main point of execution.
##### utility.py - This file has code for utilities.

### Directories
The directories listed are discussed in brief here

| Directory | Contents | Contributor |
| ------ | ------ | ------ |
|  AStar  | Code for AStar Algorithm implementaiton.| Shikher Singh
|  Iterative Deepening Algorithm  | Code for Iterative Deepening Algorithm implementaiton.| Tanvi Bagla
|  UniformedCostSearch  | Code for Uniformed Cost Search Algorithm implementaiton.| Vishal
|  Report  | This directory contains the report.| Abhinav Gandhi

### Execution
1. Navigate to the directory of the desired algorithm 
2. Run `python TaskExecution.py test_case_no start_state` to generate a result file.
    Sample command: `python TaskExecution.py 2 1,3,2,4,5,0,6,7,8`.

| Algorithm | Command | Parameter | Initial State |
| ------ | ------ | ------ | ------ |
| AST | python TaskExecution.py | ast
| UCS | python TaskExecution.py | 
| IDFFS | python TaskExecution.py |

## Version Log




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen.)


   [repo]: <https://github.com/singh0021/AI_Project>
   [N-puzzle]: <http:mypuzzle.org/sliding>
   
