import sys, collections

with open(sys.argv[1]) as file:
    joltages = list(map(int, file))

joltages.sort()
differences = [j2 - j1 for j1, j2 in zip([0] + joltages, joltages)]
differences.append(3)
assert all(diff in (1, 2, 3) for diff in differences)
counts = collections.Counter(differences)

print(counts)

print(counts[1] * counts[3])
