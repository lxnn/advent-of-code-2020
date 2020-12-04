import sys

def entries(line_iterable):
    entry = {}
    for line in line_iterable:
        if line.strip() == '':
            if entry:
                yield entry
                entry = {}
            continue
        for fieldstr in line.split():
            field, _, value = fieldstr.partition(':')
            entry[field] = value
    if entry:
        yield entry

required_fields = set('byr iyr eyr hgt hcl ecl pid'.split())
optional_fields = {'cid'}

valid_count = 0
with open(sys.argv[1]) as file:
    for entry in entries(file):
        fields = set(entry.keys())
        isvalid = (
                required_fields.issubset(fields)
            and fields.issubset(required_fields | optional_fields)
        )
        if isvalid:
            valid_count += 1

print(valid_count)
