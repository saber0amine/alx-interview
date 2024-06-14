#!/usr/bin/python3
"""0. N queens
alx interview task"""


import sys


def isNvalid():
    """checks if N is valid"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])

    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solveNqueen(n)


def solveNqueen(n: int):
    """main function to solve the N queen problem"""
    col = set()
    posDiag = set()  # r+c
    negDiag = set()  # r-c
    resp = []

    def print_sol(resp):
        for row in resp:
            print(row)

    def backtrack(r, solution):
        """implementation for backtrack algo"""
        if r == n:
            resp.append(solution)
            return

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)

            backtrack(r + 1, solution + [[r, c]])

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)

    backtrack(0, [])
    print_sol(resp)


if __name__ == "__main__":
    isNvalid()
