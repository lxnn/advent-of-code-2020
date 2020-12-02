#!/usr/bin/env python3

from collections import Counter

num_valid = 0

with open('input.txt') as f:
    for line in f:
        policy, _, password = line.partition(':')
        interval, char      = policy.split()
        low, _, high        = interval.partition('-')
        acceptable_range    = range(int(low), int(high)+1)
        if password.count(char) in acceptable_range:
            num_valid += 1

print(num_valid)

