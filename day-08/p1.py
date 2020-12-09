import sys

with open(sys.argv[1]) as file:
    program = [
        (inst, int(arg))
        for inst, arg in map(str.split, file)
    ]

pc, acc = 0, 0
visited = set()

while pc not in visited:
    visited.add(pc)
    inst, arg = program[pc]
    if inst == 'jmp':
        pc += arg
    elif inst == 'acc':
        acc += arg
        pc += 1
    elif inst == 'nop':
        pc += 1
    else:
        raise Exception(f"Invalid instruction {inst!r}")

print(acc)
