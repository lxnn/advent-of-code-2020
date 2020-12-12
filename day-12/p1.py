import sys
from math import e, pi, radians

with open(sys.argv[1]) as file:
    instructions = [(line[0], int(line[1:])) for line in file]

position, waypoint = 0+0j, 1+0j
directions = dict(N=0+1j, E=1+0j, S=0-1j, W=-1+0j)

for op, arg in instructions:
    if op in directions:
        position += arg * directions[op]
    elif op == 'F':
        position += arg * waypoint
    elif op == 'L':
        waypoint *= e ** (+radians(arg) * 1j)
    elif op == 'R':
        waypoint *= e ** (-radians(arg) * 1j)
    else:
        assert False

print(round(abs(position.real) + abs(position.imag), 2))
