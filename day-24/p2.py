from utils import *

try:
    with open(sys.argv[1]) as file:
        raw = file.read()
except IndexError:
    raw = sys.stdin.read()

sequences = [
    re.findall(r'se|sw|ne|nw|e|w', line)
    for line in lines(raw)
]

vectors = dict(
    ne  = -1 + 0j,
    e   =  0 + 1j,
    se  = +1 + 1j,
    sw  = +1 + 0j,
    w   =  0 - 1j,
    nw  = -1 - 1j,
)

def sequence_to_coord(sequence):
    coord = 0 + 0j
    for inst in sequence:
        coord += vectors[inst]
    return coord

def neighbours(coord):
    return {
        coord + vector
        for vector in vectors.values()
    }

tile_flips = Counter(map(sequence_to_coord, sequences))
black_tiles = {tile for tile, flips in tile_flips.items() if flips % 2 == 1}

for day in range(100):
    tiles_of_interest = set.union(*map(neighbours, black_tiles))
    black_tiles = {
        tile
        for tile in tiles_of_interest
        if len(neighbours(tile) & black_tiles) in (
            (1, 2) if tile in black_tiles else (2,)
        )
    }

print(len(black_tiles))
