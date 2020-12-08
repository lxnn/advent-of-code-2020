import sys, re
from typing import NamedTuple, Callable


REQUIRED_FIELDS = dict(
    byr = lambda s: 1920 <= int(s) <= 2002,
    iyr = lambda s: 2010 <= int(s) <= 2020,
    eyr = lambda s: 2020 <= int(s) <= 2030,
    hgt = lambda s: bool(
                (m := re.fullmatch(r"([0-9]+)(cm|in)", s))
            and (r := {'cm': range(150, 194), 'in': range(59, 77)}[m.group(2)])
            and (int(m.group(1)) in r)
        ),
    hcl = lambda s: re.fullmatch(r"#[0-9a-f]{6}", s),
    ecl = lambda s: s in "amb blu brn gry grn hzl oth".split(),
    pid = lambda s: re.fullmatch(r"[0-9]{9}", s),
)


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


def isvalid(entry):
    for field, validator in REQUIRED_FIELDS.items():
        if field not in entry:
            print(f"Missing field: {field}")
            return False
        if not validator(entry[field]):
            print(f"Invalid value {entry[field]} for field {field}.")
            return False
    return True


with open(sys.argv[1]) as file:
    valid_count = sum(
        isvalid(entry)
        for entry in entries(file)
    )


print(valid_count)
