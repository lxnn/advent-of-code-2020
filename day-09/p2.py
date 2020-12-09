import sys, collections

def two_sum(iterable, target):
    seen = set()
    for num in iterable:
        if target - num in seen:
            return True
        seen.add(num)
    return False


def first_non_twosum_of_previous(numbers, lookbehind):
    queue = collections.deque(maxlen=lookbehind)
    for num in numbers:
        if len(queue) == queue.maxlen and not two_sum(queue, num):
            return num
        queue.append(num)

def contiguous_sum(numbers, target):
    queue = collections.deque()
    total = 0
    for num in numbers:
        total += num
        queue.append(num)
        while total > target:
            total -= queue.popleft()
        if total == target and len(queue) > 1:
            return list(queue)

with open(sys.argv[1]) as file:
    numbers = list(map(int, file))

lookbehind = int(sys.argv[2])

target = first_non_twosum_of_previous(numbers, lookbehind)
numset = contiguous_sum(numbers, target)

print(min(numset) + max(numset))
