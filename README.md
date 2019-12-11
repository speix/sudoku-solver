# Sudoku solver (CSP approach)
A.I - Implemented AC3, Backtracking and Forward Checking algorithms in combination with Most Constrained Variable (a.k.a MRV) and Least Constraining Value (a.k.a LCV) heuristics. 

In fact, the above algorithms and heuristics are essential when it comes το solving any Constraint Satisfaction problem (a.k.a CSPs). 
Performance-wise, the solver was able to solve 400 sudoku boards in approx. 45 seconds.  
The script prints the board to output.txt


### Algorithms
```
AC3 (Reduces the domain for each variable based on constraints (arcs) without breaking the consistency)
Backtracking (In a nutshell its a Depth-First Search with the ability to move backwards when there is no solution)
Forward Checking (Eliminate the possibilities that do not match the constraints from the domains of unassigned variables)
MRV (Choose the variable with the fewest legal moves)
LCV (Choose the value that rules out the fewest values in the remaining variables)
```
### Usage
```
python driver.py 000530000005000600000190503000004000000000164100370800008000040010000008004700921
```
### Results
![alt tag](https://s3.eu-central-1.amazonaws.com/files.supergramm.com/main/images/github/sudokuresults.jpg)
