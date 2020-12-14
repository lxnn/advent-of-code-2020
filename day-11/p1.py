import sys, re

with open(sys.argv[1]) as file:
    state = list(map(list, map(str.strip, file)))

def newval(state, row, col):
    seatstate = state[row][col]
    if seatstate == '.':
        return '.'
    neighbours = [
        state[row+drow][col+dcol]
        for drow in (-1, 0, 1)
        for dcol in (-1, 0, 1)
        if 0 <= row+drow < len(state)
        if 0 <= col+dcol < len(state[0])
        if drow != 0 or dcol != 0
    ]
    num_occupied = neighbours.count('#')
    if seatstate == 'L' and num_occupied == 0:
        return '#'
    elif seatstate == '#' and num_occupied >= 4:
        return 'L'
    else:
        return seatstate

def update(state):
    return [
        [
            newval(state, i, j)
            for j, val in enumerate(row)
        ]
        for i, row in enumerate(state)
    ]

while True:
    new_state = update(state)
    if new_state == state:
        break
    state = new_state

print(sum(
    row.count('#')
    for row in state
))

