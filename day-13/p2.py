import sys

with open(sys.argv[1]) as file:
    arrival = int(file.readline())
    schedule = [
        (i, int(entry))
        for i, entry in enumerate(file.readline().split(','))
        if entry != 'x'
    ]

# Assume numbers are prime.

product = 1
n = 0

for i, x in schedule:
    while n % x != -i % x:
        n += product
    product *= x
    assert n < product

print(n)
