import argparse
from sudoku import Sudoku


def ac3(sudoku):

    queue = list(sudoku.constraints)

    while queue:

        xi, xj = queue.pop(0)

        if revise(sudoku, xi, xj):

            if len(sudoku.domains[xi]) == 0:
                return False

            for xk in sudoku.neighbors[xi]:
                if xk != xi:
                    queue.append([xk, xi])

    return True


def revise(sudoku, xi, xj):

    revised = False

    for x in sudoku.domains[xi]:
        if not any([sudoku.constraint(x, y) for y in sudoku.domains[xj]]):
            sudoku.domains[xi].remove(x)
            revised = True

    return revised


def backtrack(assignment, sudoku):

    if len(assignment) == len(sudoku.variables):
        return assignment

    var = select_unassigned_variable(assignment, sudoku)

    for value in order_domain_values(sudoku, var):

        if sudoku.consistent(assignment, var, value):

            sudoku.assign(var, value, assignment)

            result = backtrack(assignment, sudoku)
            if result:
                return result

            sudoku.unassign(var, assignment)

    return False


# Most Constrained Variable heuristic
# Pick the unassigned variable that has fewest legal values remaining.
def select_unassigned_variable(assignment, sudoku):
    unassigned = [v for v in sudoku.variables if v not in assignment]
    return min(unassigned, key=lambda var: len(sudoku.domains[var]))


# Least Constraining Value heuristic
# Prefers the value that rules out the fewest choices for the neighboring variables in the constraint graph.
def order_domain_values(sudoku, var):
    if len(sudoku.domains[var]) == 1:
        return sudoku.domains[var]

    return sorted(sudoku.domains[var], key=lambda val: sudoku.conflicts(sudoku, var, val))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('board')
    args = parser.parse_args()

    sudoku = Sudoku(args.board)

    if ac3(sudoku):

        if sudoku.solved():

            output = open('output.txt', 'w')
            for var in sudoku.variables:
                output.write(str(sudoku.domains[var][0]))
            output.close()

        else:

            assignment = {}

            for x in sudoku.variables:
                if len(sudoku.domains[x]) == 1:
                    assignment[x] = sudoku.domains[x][0]

            assignment = backtrack(assignment, sudoku)

            for d in sudoku.domains:
                sudoku.domains[d] = assignment[d] if len(d) > 1 else sudoku.domains[d]

            if assignment:

                output = open('output.txt', 'w')
                for var in sudoku.variables:
                    output.write(str(sudoku.domains[var]))
                output.close()

            else:
                print "No solution exists"

if __name__ == '__main__':
    main()
