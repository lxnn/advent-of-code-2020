import sys
from collections import deque

try:
    with open(sys.argv[1]) as file:
        raw = file.read()
except IndexError:
    raw = sys.stdin.read()

p1raw, p2raw = map(str.splitlines, raw.split('\n\n'))

p1 = deque(map(int, p1raw[1:]))
p2 = deque(map(int, p2raw[1:]))

print(p1, p2)

def get_score(deck):
    return sum(
        i * card
        for i, card in enumerate(reversed(deck), start=1)
    )

def play(p1, p2):
    while True:
        if not p1:
            return 2, get_score(p2)
        elif not p2:
            return 1, get_score(p1)
        elif p1[0] >= p2[0]:
            p1.extend([p1.popleft(), p2.popleft()])
        else:
            p2.extend([p2.popleft(), p1.popleft()])

winner, score = play(p1, p2)

print(winner, score)
