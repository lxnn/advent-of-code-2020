import sys, collections, itertools, functools, math
from math import radians, sin, cos

with open(sys.argv[1]) as file:
    instructions = [
        (line[0], int(line[1:]))
        for line in file
    ]

x, y, dx, dy = 0., 0., 10., 1.

for op, arg in instructions:
    if op == 'N':
        dy += arg
    elif op == 'S':
        dy -= arg
    elif op == 'E':
        dx += arg
    elif op == 'W':
        dx -= arg
    elif op == 'F':
        x += arg * dx
        y += arg * dy
    elif op == 'L':
        rad = radians(arg)
        dx, dy = (
            + dx * cos(rad) - dy * sin(rad),
            + dx * sin(rad) + dy * cos(rad)
        )
    elif op == 'R':
        rad = radians(arg)
        dx, dy = (
            + dx * cos(rad) + dy * sin(rad),
            - dx * sin(rad) + dy * cos(rad)
        )
    else:
        assert False

ans = abs(x) + abs(y)
print(f"{x=:.2f} {y=:.2f} {ans=:.2f}")
