import sys, math
from dataclasses    import dataclass
from itertools      import islice, chain
from typing         import Optional

try:
    with open(sys.argv[1]) as file:
        raw = file.read()
except IndexError:
    raw = sys.stdin.read()

nums = list(map(int, raw.strip()))
high, iterations = max(nums), 100

@dataclass
class Node:
    val:    int
    next:   Optional['Node']    = None

class CircularLL:

    def __init__(self, vals):
        self.table = dict()
        prev = None
        for val in vals:
            assert val not in self.table
            new_node = Node(val)
            if prev:
                prev.next = new_node
            else:
                first_node = new_node
            self.table[val] = new_node
            prev = new_node
        prev.next = first_node

    def __getitem__(self, key):
        return self.table[key]

    def iterfrom(self, val):
        node = self[val]
        while True:
            yield node.val
            node = node.next

ll = CircularLL(nums)
current = nums[0]

for move in range(iterations):
    current, *pickup, after = islice(ll.iterfrom(current), 5)
    ll[current].next = ll[after]
    dest = current - 1 or high
    while dest in pickup:
        dest = dest - 1 or high
    dest, after_dest = islice(ll.iterfrom(dest), 2)
    ll[dest].next, ll[pickup[-1]].next = ll[pickup[0]], ll[after_dest]
    current = ll[current].next.val

print(*islice(ll.iterfrom(1), 1, len(nums)), sep='')
