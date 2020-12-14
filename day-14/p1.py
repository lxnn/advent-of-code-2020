import sys, re

def applymask(value, mask):
    bits = f"{value:036b}"
    return int(''.join(
        bit if maskbit == 'X' else maskbit
        for bit, maskbit in zip(bits, mask)
    ), base=2)

mem = dict()

with open(sys.argv[1]) as file:
    for line in file:
        if m := re.match(r"mask = ([0-9X]+)", line):
            mask = m.group(1)
        elif m := re.match(r"mem\[([0-9]+)\] = ([0-9]+)", line):
            address, value = int(m.group(1)), int(m.group(2))
            mem[address] = applymask(value, mask)

print(sum(mem.values()))
