# sudoku
A.I - Implemented AC3, Backtracking and Forward Checking algorithms in combination with Most Constrained Variable (a.k.a MRV) and Least Constraining Value (a.k.a LCV) heuristics. 

In fact, the above algorithms and heuristics are essential when it comes το solving any Constraint Satisfaction problem (a.k.a CSPs). 
Performance-wise, the solver was able to solve 400 sudoku boards in approx. 40 seconds.  
The script prints the board to output.txt


### Algorithms
```
AC3 (Arc Consistency)
Backtracking (In a nutshell its a Depth-First Search algorithm with the ability to move backwards when there is no solution)
Forward Checking (A-Star Search)
ida (Iterative-Deepening-ΑStar Search)
```
### Usage
```
python driver.py 000530000005000600000190503000004000000000164100370800008000040010000008004700921
```
### Results
```
path_to_goal: ['Right', 'Down', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Down', 'Left', 'Up', 'Right', 'Down', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Right', 'Up', 'Right', 'Down', 'Left', 'Down', 'Right', 'Up', 'Up', 'Left', 'Left']
cost_of_path: 30
nodes_expanded: 12893
fringe_size: 6327
max_fringe_size: 6328
search_depth: 30
max_search_depth: 30
running_time: 1.80822521
max_ram_usage: 7.44400000
```
