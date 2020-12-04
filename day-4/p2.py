import sys, re
from typing import NamedTuple, Callable


class FieldSpec(NamedTuple):
    required:   bool
    validator:  Callable[[str], bool]


FIELDS = dict(
    byr = FieldSpec(
        required    = True,
        validator   = lambda string: bool(
                            (m := re.fullmatch(r"[0-9]{4}", string))
                        and (1920 <= int(m.group(0)) <= 2002)
                    ),
    ),
    iyr = FieldSpec(
        required    = True,
        validator   = lambda string: bool(
                            (m := re.fullmatch(r"[0-9]{4}", string))
                        and (2010 <= int(m.group(0)) <= 2020)
                    ),
    ),
    eyr = FieldSpec(
        required    = True,
        validator   = lambda string: bool(
                            (m := re.fullmatch(r"[0-9]{4}", string))
                        and (2020 <= int(m.group(0)) <= 2030)
                    ),
    ),
    hgt = FieldSpec(
        required    = True,
        validator   = lambda string: bool(
                            (m := re.fullmatch(r"([0-9]+)(cm|in)", string))
                        and int(m.group(1)) in {
                                'cm': range(150, 194),
                                'in': range(59, 77),
                            }[m.group(2)]
                    ),
    ),
    hcl = FieldSpec(
        required    = True,
        validator   = lambda string: bool(
                        re.fullmatch(r"#[0-9a-f]{6}", string)
                    ),
    ),
    ecl = FieldSpec(
        required    = True,
        validator   = lambda string: bool(
                        re.fullmatch(r"amb|blu|brn|gry|grn|hzl|oth", string)
                    ),
    ),
    pid = FieldSpec(
        required    = True,
        validator   = lambda string: bool(re.fullmatch(r"[0-9]{9}", string)),
    ),
    cid = FieldSpec(
        required    = False,
        validator   = lambda string: True,
    ),
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
    for fieldname, spec in FIELDS.items():
        if fieldname not in entry:
            if spec.required:
                print(f"Missing field: {fieldname}")
                return False
            continue
        if not spec.validator(entry[fieldname]):
            print(f"Invalid value {entry[fieldname]} for field {fieldname}.")
            return False
    return True


with open(sys.argv[1]) as file:
    valid_count = sum(
        isvalid(entry)
        for entry in entries(file)
    )


print(valid_count)
