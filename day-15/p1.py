import sys

with open(sys.argv[1]) as file:
    numbers = list(map(int, file.read().split(',')))

last_seen = dict()

for i in range(2020 - 1):
    if i < len(numbers):
        num = numbers[i]
    if num in last_seen:
        nextnum = i - last_seen[num]
    else:
        nextnum = 0
    last_seen[num] = i
    num = nextnum

print(num)
