import sys, collections, functools

if len(sys.argv) >= 2:
    with open(sys.argv[1]) as file:
        rawinput = file.read()
else:
    rawinput = sys.stdin.read()

rawrules, rawmessages = rawinput.split('\n\n')

rawrules = rawrules.replace("8: 42\n", "8: 42 | 42 8\n")
rawrules = rawrules.replace("11: 42 31\n", "11: 42 31 | 42 11 31\n")

terminals = dict()
nonterminals = collections.defaultdict(set)

for rawrule in rawrules.splitlines():
    lhs, rhs = map(str.strip, rawrule.split(':'))
    if rhs.startswith('"'):
        terminals[lhs] = rhs.strip('"')
    else:
        for rawpattern in map(str.strip, rhs.split('|')):
            nonterminals[lhs].add(tuple(rawpattern.split()))

messages = rawmessages.splitlines()

print(terminals)
print(nonterminals)

@functools.lru_cache(None)
def match(message, lhs):
    if lhs in nonterminals:
        res = any(
            matchpattern(message, rhs)
            for rhs in nonterminals[lhs]
        )
    else:
        res = message == terminals[lhs]
    # print(f"match{message, lhs} -> {res}")
    return res

@functools.lru_cache(None)
def matchpattern(message, pattern):
    if not pattern:
        return message == ''
    first, *rest = pattern
    res = any(
        match(left, first) and matchpattern(right, tuple(rest))
        for left, right in splits(message)
    )
    # print(f"matchpattern{message, pattern} -> {res}")
    return res

def splits(message):
    for i in range(len(message) + 1):
        yield message[:i], message[i:]

print(sum(match(message, '0') for message in messages))

