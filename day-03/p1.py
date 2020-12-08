#!/usr/bin/env python3

import sys

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

position = i, j = (0, 0)
tree_count = 0
while i < M:
    tree_count += grid[i][j%N] == TREE
    position = i, j = i+DI, j+DJ

print(tree_count)
