#!/usr/bin/python3
"""0. N queens
"""
import sys


sol = []
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def isSafe(mat, r, c):
    """Function to check if two queens threaten each other or not
    """
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def queens_position(mat):
    """Take position of queen
    """
    global sol
    if mat:
        for t in range(len(mat)):
            for h in range(len(mat[t])):
                if mat[t][h] == 'Q':
                    sol.append([t, h])
        print(sol)
        sol = []


def nQueen(mat, r):
    """place the queens on the board
    """
    # if `N` queens are placed successfully, print the solution
    if r == len(mat):
        # sol.append(mat.copy())
        # printSolution(mat)
        return mat

    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(len(mat)):

        # if no two queens threaten each other
        if isSafe(mat, r, i):
            # place queen on the current square
            mat[r][i] = 'Q'
            # sol.append([r,i])

            # recur for the next row
            tmp = nQueen(mat, r + 1)
            queens_position(tmp)

            # backtrack and remove the queen from the current square
            mat[r][i] = '–'


if __name__ == '__main__':

    # `N × N` chessboard

    # `mat[][]` keeps track of the position of queens in
    # the current configuration
    mat = [['–' for x in range(n)] for y in range(n)]

    nQueen(mat, 0)
