import sys, collections

queue = collections.deque(maxlen=int(sys.argv[2]))

def twosum(iterable, target):
    seen = set()
    for num in iterable:
        if target - num in seen:
            return True
        seen.add(num)
    return False

with open(sys.argv[1]) as file:
    for num in map(int, file):
        if len(queue) == queue.maxlen and not twosum(queue, num):
            print(num)
        queue.append(num)

