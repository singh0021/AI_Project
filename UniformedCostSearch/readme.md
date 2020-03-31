## Please run below 4 test cases and to generate result files
> **testScript.sh** : Run for executing all 4 Testcases

> **utility.py** : this file contains queue and Stack classes to be used in Search Algorithms

> **SearchAlgo.py** : This file actually implements Uniform Cost Search algorithm

> **TaskExecution.py**: This is the driver file to be run for algorithm

> **path_to_goal**: the sequence of moves taken to reach the goal

> **cost_of_path**: the number of moves taken to reach the goal

> **nodes_expanded**: the number of nodes that have been expanded

> **search_depth**: the depth within the search tree when the goal node is found

> **max_search_depth**:  the maximum depth of the search tree in the lifetime of the algorithm

> **running_time**: the total running time of the search instance, reported in seconds

> **max_ram_usage**: the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes

## cmd format : 
> python TaskExecution.py  ucs  [Testcase Number] [Test Case Sequence]

### Test Case 1  => Result_test1.txt
> python TaskExecution.py ucs 1 1,2,5,3,4,0,6,7,8

### Test Case 2 => Result_test2.txt
> python TaskExecution.py ucs 2 3,1,2,0,4,5,6,7,8

### Test Case 3 => Result_test3.txt
> python TaskExecution.py ucs 3 3,1,2,4,5,0,6,7,8

### Test Case 4 => Result_test4.txt
> python TaskExecution.py ucs 4 1,2,5,0,3,4,6,7,8
 