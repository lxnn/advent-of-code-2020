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

def sequence_to_coord(sequence):
    i, j = 0, 0
    for inst in sequence:
        if inst == 'ne':
            i -= 1
        elif inst == 'e':
            j += 1
        elif inst == 'se':
            i += 1
            j += 1
        elif inst == 'sw':
            i += 1
        elif inst == 'w':
            j -= 1
        elif inst == 'nw':
            i -= 1
            j -= 1
        else:
            assert False
    return i, j

tile_flips = Counter(map(sequence_to_coord, sequences))

black_tiles = {tile for tile, flips in tile_flips.items() if flips % 2 == 1}

print(len(black_tiles))
