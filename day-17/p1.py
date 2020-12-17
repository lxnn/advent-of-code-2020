import sys

ACTIVE, INACTIVE = '#.'

with open(sys.argv[1]) as file:
    initial_state = {
        (i, j, 0)
        for i, row in enumerate(file)
        for j, val in enumerate(row)
        if val == ACTIVE
    }

def neighbors(cube):
    i, j, k = cube
    return {
        (i+di, j+dj, k+dk)
        for di in (-1, 0, 1)
        for dj in (-1, 0, 1)
        for dk in (-1, 0, 1)
        if di != 0 or dj != 0 or dk != 0
    }

def num_active_neighbors(cube, active_cubes):
    return sum(
        neighbor in active_cubes
        for neighbor in neighbors(cube)
    )

active_cubes = initial_state.copy()

for cycle in range(6):
    inactive_cubes_of_interest = (
            set.union(*map(neighbors, active_cubes))
        -   active_cubes
    )
    activated_cubes = {
        cube
        for cube in inactive_cubes_of_interest
        if num_active_neighbors(cube, active_cubes) == 3
    }
    deactivated_cubes = {
        cube
        for cube in active_cubes
        if num_active_neighbors(cube, active_cubes) not in (2, 3)
    }
    active_cubes |= activated_cubes
    active_cubes -= deactivated_cubes

print(len(active_cubes))

