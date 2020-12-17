import sys, collections, itertools

with open(sys.argv[1]) as file:
    fields_text, ticket_text, nearby_text = file.read().split('\n\n')

fields = dict()
for line in fields_text.splitlines():
    name, _, raw_ranges = map(str.strip, line.partition(':'))
    fields[name] = []
    for raw_range in raw_ranges.split('or'):
        low, _, high = raw_range.partition('-')
        fields[name].append(range(int(low), int(high)+1))

raw_ticket = ticket_text.splitlines()[1]
my_ticket = list(map(int, raw_ticket.split(',')))

nearby_tickets = [
    list(map(int, raw_ticket.split(',')))
    for raw_ticket in nearby_text.splitlines()[1:]
]

completely_invalid_tickets = [
    ticket
    for ticket in nearby_tickets
    if any(
        all(
            value not in range_
            for field, ranges in fields.items()
            for range_ in ranges
        )
        for value in ticket
    )
]

scanning_error_rate = sum(
    value
    for ticket in nearby_tickets
    for value in ticket
    if all(
        value not in range_
        for field, ranges in fields.items()
        for range_ in ranges
    )
)

print(scanning_error_rate)
