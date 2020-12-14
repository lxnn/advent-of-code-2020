import sys, re, itertools

with open(sys.argv[1]) as file:
    state = list(map(list, map(str.strip, file)))

EMPTY, OCCUPIED, FLOOR = 'L', '#', '.'

def visible_seats(state, i, j):
    m, n = len(state), len(state[0])
    vectors = (
        (di, dj)
        for di in (-1, 0, 1)
        for dj in (-1, 0, 1)
        if di != 0 or dj != 0
    )
    for di, dj in vectors:
        oi, oj = i+di, j+dj
        while 0 <= oi < m and 0 <= oj < n:
            if state[oi][oj] in (EMPTY, OCCUPIED):
                yield state[oi][oj]
                break
            oi += di
            oj += dj

def nextval(state, i, j):
    seat = state[i][j]
    if seat == FLOOR:
        return FLOOR
    num_occupied = list(visible_seats(state, i, j)).count('#')
    if seat == EMPTY and num_occupied == 0:
        return OCCUPIED
    elif seat == OCCUPIED and num_occupied >= 5:
        return EMPTY
    else:
        return seat

def update(state):
    return [
        [
            nextval(state, i, j)
            for j, val in enumerate(row)
        ]
        for i, row in enumerate(state)
    ]

def solve(state):
    while True:
        new_state = update(state)
        if new_state == state:
            break
        state = new_state
    return sum(
        row.count(OCCUPIED)
        for row in state
    )

print(solve(state))
