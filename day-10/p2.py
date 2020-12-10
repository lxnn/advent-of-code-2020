import sys, collections

with open(sys.argv[1]) as file:
    joltages = set(map(int, file))

joltages.add(0)
device = max(joltages) + 3

table = collections.defaultdict(int)
table[device] = 1

for j in reversed(sorted(joltages)):
    table[j] = sum(
        table[j + dj]
        for dj in (1, 2, 3)
    )

print(table[0])
