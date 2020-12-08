import sys
from functools import reduce

def groups(line_iterable):
    group = []
    for line in line_iterable:
        if line.strip() == '':
            if group:
                yield group
                group = []
            continue
        group.append(set(line.strip()))
    if group:
        yield group

total = 0

with open(sys.argv[1]) as file:
    for group in groups(file):
        total += len(reduce(set.intersection, group))

print(total)
