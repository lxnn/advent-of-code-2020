#!/usr/bin/env python3

import sys

num_valid = 0

with open(sys.argv[1]) as file:
    for line in file:
        policy, _, password = map(str.strip, line.partition(':'))
        positions, char     = map(str.strip, policy.split())
        positions           = list(map(int, positions.split('-')))
        values              = [password[i-1] for i in positions]
        if values.count(char) == 1:
            num_valid += 1

print(num_valid)

