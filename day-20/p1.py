import sys, collections, functools, itertools, math, statistics, re, copy
import numpy as np

if len(sys.argv) >= 2:
    with open(sys.argv[1]) as file:
        rawinput = file.read()
else:
    rawinput = sys.stdin.read()

tiles = dict()

for rawtile in rawinput.split('\n\n'):
    rawtilelines = rawtile.splitlines()
    if not rawtilelines:
        continue
    number = int(re.match(r"Tile (\d+):", rawtilelines[0]).group(1))
    pattern = np.array(list(map(list, rawtilelines[1:]))) == '#'
    tiles[number] = pattern

TransformedTile = collections.namedtuple('TransTile', 'id rotation flipped')

N, E, S, W = 0, 1, 2, 3

@functools.lru_cache(None)
def edge(tt, cardinal):
    # Flip in the E-W direction, then rotate the tile clockwise.
    if tt.flipped:
        cardinal = [N, W, S, E][(cardinal - tt.rotation) % 4]
    else:
        cardinal = [N, E, S, W][(cardinal - tt.rotation) % 4]
    if cardinal == N:
        unflipped = tiles[tt.id][0,:]
    elif cardinal == E:
        unflipped = tiles[tt.id][:,-1]
    elif cardinal == S:
        unflipped = tiles[tt.id][-1,::-1]
    elif cardinal == W:
        unflipped = tiles[tt.id][::-1,0]
    # Traverse the edge in an anit-clockwise direction if flipped, otherwise a
    # clockwise direction.
    if tt.flipped:
        return unflipped[::-1]
    else:
        return unflipped

@functools.lru_cache(None)
def stackv(tt1, tt2):
    return (edge(tt1, S)[::-1] == edge(tt2, N)).all()

@functools.lru_cache(None)
def stackh(tt1, tt2):
    return (edge(tt1, E)[::-1] == edge(tt2, W)).all()

@functools.lru_cache(None)
def match(tt1, tt2, cardinal):
    if cardinal == N:
        return stackv(tt2, tt1)
    if cardinal == S:
        return stackv(tt1, tt2)
    if cardinal == W:
        return stackh(tt2, tt1)
    if cardinal == E:
        return stackh(tt1, tt2)

K = int(math.sqrt(len(tiles)))

def neighbours(coord):
    i, j = coord
    return (
        ((i+di, j+dj), cardinal)
        for di, dj, cardinal in [
            (-1, 0, N),
            (0, 1, E),
            (1, 0, S),
            (0, -1, W),
        ]
        if 0 <= i+di < K
        if 0 <= j+dj < K
    )

transformed_tiles = {
    TransformedTile(tileid, rotation, flipped)
    for tileid in tiles
    for rotation in range(4)
    for flipped in range(2)
}

coordinates = {
    (i, j)
    for i in range(K)
    for j in range(K)
}

def mhatnorm(coord):
    i, j = coord
    return abs(i) + abs(j)

def solve(state, coord_stack):
    remaining_coords = coordinates - set(state)
    if not remaining_coords:
        return state
    coord = min(remaining_coords, key=mhatnorm)
    possibilities = (
        tt
        for tt in transformed_tiles
        if not any(
            tt.id == other.id
            for other in state.values()
        )
        if all(
            match(tt, state[neighbour], cardinal)
            for neighbour, cardinal in neighbours(coord)
            if neighbour in state
        )
    )
    for tt in possibilities:
        state[coord] = tt
        if solve(state, coord_stack):
            return state
        del state[coord]

solution = solve({}, sorted(coordinates, key=mhatnorm))
print(solution)
print(math.prod(
    solution[i, j].id
    for i in (0, K-1)
    for j in (0, K-1)
))

