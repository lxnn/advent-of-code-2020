import sys

try:
    with open(sys.argv[1]) as file:
        raw = file.read()
except IndexError:
    raw = sys.stdin.read()

MODULUS = 20201227
SUBJECT_NO = 7

card_public, door_public = map(int, raw.splitlines())

def get_secret(public):
    num_loops = 1
    number = SUBJECT_NO
    while True:
        if public == number:
            return num_loops
        number *= SUBJECT_NO
        number %= MODULUS
        num_loops += 1

card_loops = get_secret(card_public)
door_loops = get_secret(door_public)


key = pow(card_public, door_loops, mod=MODULUS)

assert key == pow(door_public, card_loops, mod=MODULUS)

print(f"{card_loops=} {door_loops=} {key=}")
