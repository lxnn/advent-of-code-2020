import sys

NUM_ROW_BITS = 7
NUM_COL_BITS = 3

def id(code):
    row_binary = code[:NUM_ROW_BITS].replace('F', '0').replace('B', '1')
    col_binary = code[NUM_ROW_BITS:].replace('L', '0').replace('R', '1')
    return int(row_binary, base=2) * 2**NUM_COL_BITS + int(col_binary, base=2)

with open(sys.argv[1]) as file:
    max_id = max(map(id, file))

print(max_id)
