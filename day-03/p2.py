#!/usr/bin/env python3

import sys, operator, functools

OPEN = '.'
TREE = '#'
OFFSET = DI, DJ = (1, 3)

with open(sys.argv[1]) as file:
    grid = [
        [
            char
            for char in line.strip()
        ]
        for line in file
    ]

M, N = len(grid), len(grid[0])

def count_trees(start, slope):
    i, j    = start
    di, dj  = slope
    count   = 0
    while i < M:
        count += grid[i][j%N] == TREE
        i, j = i+di, j+dj
    return count

def product(numbers):
    return functools.reduce(operator.mul, numbers, 1)

slopes      = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
tree_counts = [count_trees((0, 0), slope) for slope in slopes]

print(product(tree_counts))
