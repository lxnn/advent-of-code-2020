import sys, re

def applymask(value, mask):
    bits = f"{value:036b}"
    nums = ['']
    for bit, maskbit in zip(bits, mask):
        if maskbit == '0':
            nums = [
                num + bit
                for num in nums
            ]
        elif maskbit == '1':
            nums = [
                num + '1'
                for num in nums
            ]
        elif maskbit == 'X':
            nums = [
                num + newbit
                for num in nums
                for newbit in '01'
            ]
        else:
            assert False
    return (int(num, base=2) for num in nums)

mem = dict()

with open(sys.argv[1]) as file:
    for line in file:
        if m := re.match(r"mask = ([0-9X]+)", line):
            mask = m.group(1)
        elif m := re.match(r"mem\[([0-9]+)\] = ([0-9]+)", line):
            unmasked_address, value = int(m.group(1)), int(m.group(2))
            for address in applymask(unmasked_address, mask):
                mem[address] = value

print(sum(mem.values()))
