import sys, collections, itertools, functools, math

with open(sys.argv[1]) as file:
    instructions = [
        (line[0], int(line[1:]))
        for line in file
    ]

x, y, heading = 0., 0., 90.

for op, arg in instructions:
    if op == 'N':
        y += arg
    elif op == 'S':
        y -= arg
    elif op == 'E':
        x += arg
    elif op == 'W':
        x -= arg
    elif op == 'F':
        x += arg * math.sin(math.radians(heading))
        y += arg * math.cos(math.radians(heading))
    elif op == 'L':
        heading -= arg
        heading %= 360
    elif op == 'R':
        heading += arg
        heading %= 360
    else:
        assert False

ans = abs(x) + abs(y)
print(f"{x=:.2f} {y=:.2f} {ans=:.2f}")
