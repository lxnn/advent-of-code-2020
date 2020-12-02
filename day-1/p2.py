#!/usr/bin/env python3

with open('input.txt') as file:
    nums = list(map(int, file))

target = 2020

seen = set()
for i, x in enumerate(nums):
    for j, y in enumerate(nums[i+1:], i+1):
        complement = target - (x + y)
        if complement in seen:
            print(x * y * complement)
    seen.add(x)

