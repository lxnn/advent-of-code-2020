import sys, collections, itertools, functools, operator, math, random, re

from string         import ascii_lowercase as alphabet, digits
from collections    import namedtuple, deque, defaultdict, Counter
from itertools      import islice, count, cycle, combinations, permutations
from functools      import reduce, partial, lru_cache
from operator       import itemgetter, attrgetter

fst = itemgetter(0)
snd = itemgetter(1)

def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))

def pints(string):
    return list(map(int, re.findall(r"[0-9]+", string)))

def floats(string):
    return list(map(int, re.findall(r"-?[0-9]+\.?[0-9]*", string)))

def containsany(iterable, items):
    return bool(set(items) & set(iterable))

def containsall(iterable, items):
    return set(items) <= set(iterable)

def pairs(iterable):
    it1, it2 = tee(iterable)
    next(it2, None)
    return zip(it1, it2)

def paras(string):
    return string.split('\n\n')

def lines(string):
    return string.splitlines()

def quantify(iterable, pred=bool):
    return sum(map(pred, iterable))


