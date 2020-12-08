#!/usr/bin/env python3

with open('input.txt') as file:
    nums = list(map(int, file))

target = 2020

seen = set()
for num in nums:
    complement = target - num
    if complement in seen:
        print(num * complement)
        break
    seen.add(num)

