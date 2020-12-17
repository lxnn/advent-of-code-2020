import sys, math, operator, collections, itertools

with open(sys.argv[1]) as file:
    fields_text, ticket_text, nearby_text = file.read().split('\n\n')

fields = collections.defaultdict(set)
for line in fields_text.splitlines():
    name, _, raw_ranges = map(str.strip, line.partition(':'))
    for raw_range in raw_ranges.split('or'):
        low, _, high = raw_range.partition('-')
        range_ = range(int(low), int(high) + 1)
        fields[name].add(range_)

def ticket_from_str(string):
    return tuple(map(int, string.split(',')))

my_ticket       = ticket_from_str(ticket_text.splitlines()[1])
nearby_tickets  = set(map(ticket_from_str, nearby_text.splitlines()[1:]))

def is_valid_value(value, field):
    return any(
        value in range_
        for range_ in fields[field]
    )

def is_potentially_valid_ticket(ticket):
    return all(
        any(
            is_valid_value(value, field)
            for field in fields
        )
        for value in ticket
    )

valid_tickets = set(filter(is_potentially_valid_ticket, nearby_tickets))

state = [
    {
        field
        for field in fields
        if all(
            is_valid_value(value, field)
            for value in values
        )
    }
    for values in zip(*valid_tickets)
]

while any(len(s) > 1 for s in state):
    for s1, s2 in itertools.permutations(state, 2):
        if len(s2) == 1:
            s1 -= s2

fieldnames = [
    field
    for field, in state
]

print(fieldnames)
print(my_ticket)

result = math.prod(
    value
    for field, value in zip(fieldnames, my_ticket)
    if field.startswith('departure')
)

print(result)

