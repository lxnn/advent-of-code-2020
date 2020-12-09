import sys

with open(sys.argv[1]) as file:
    program = [
        (op, int(arg))
        for op, arg in map(str.split, file)
    ]

class InfiniteLoop(Exception):
    pass

def simulate(program, pc=0, acc=0):
    visited = set()
    while pc < len(program):
        if pc in visited:
            raise InfiniteLoop()
        visited.add(pc)
        op, arg = program[pc]
        if op == 'jmp':
            pc += arg
        elif op == 'acc':
            acc += arg
            pc += 1
        elif op == 'nop':
            pc += 1
        else:
            raise Exception(f"Invalid operator {op!r}")
    return acc

for pc, (op, arg) in enumerate(program):
    if op == 'jmp':
        modified_inst = ('nop', arg)
    elif op == 'nop':
        modified_inst = ('jmp', arg)
    else:
        continue
    modified_program = program[:pc] + [modified_inst] + program[pc+1:]
    try:
        result = simulate(modified_program)
    except InfiniteLoop:
        continue
    else:
        print(
            f"Success! "
            f"Changed line {pc} from {op, arg} to {modified_inst} "
            f"and got {result}"
        )


