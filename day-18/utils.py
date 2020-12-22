"""
Utilities for Advent of Code 2020.

Author: Alex Annan

Acknowlegements:
    - Peter Norvig's AoC github page.
    - Recipes section of itertools module documentation.
"""

import sys
import typing
import math, statistics, decimal, fractions, random
import collections, heapq, bisect
import functools, itertools, operator
import datetime, time, calendar
import re, string

from math import (
    pi,
    e,
    prod,
    degrees,
    radians,
    sin,
    cos,
    tan,
    asin,
    acos,
    atan2,
)
from statistics import (
    mean,
)
from collections import (
    Counter,
    defaultdict,
    deque,
    namedtuple,
)
from itertools import (
    combinations,
    permutations,
    cycle,
    product,
    islice,
    count,
    accumulate,
    chain,
    groupby,
    tee,
    zip_longest,
)
from functools import (
    reduce,
    partial,
    lru_cache,
)
from operator import (
    itemgetter,
    attrgetter,
    add,
    sub,
    mul,
    truediv,
)
from string import (
    ascii_lowercase as alphabet,
    digits,
    hexdigits,
    octdigits,
)
from typing import (
    NamedTuple
)

# fst = operator.itemgetter(0)
# snd = operator.itemgetter(1)
# thd = operator.itemgetter(2)

def even(num):
    "Return true if the number is even"
    return num % 2 == 0

def odd(num):
    "Return true if the number is odd"
    return num % 2 == 1

def fst(iterable):
    """Get the first value of the iterable

    >>> it = iter('a b c d'.split())
    >>> fst(it)
    'a'
    """
    return next(iter(iterable))

def snd(iterable):
    """Get the second value of the iterable

    >>> it = iter('a b c d'.split())
    >>> snd(it)
    'b'
    """
    it = iter(iterable)
    next(it)
    return next(it)

def nth(iterable, n):
    """Get the nth (zero-indexed) element of the iterable

    >>> nth('a b c d'.split(), 2)
    'c'
    >>> it = iter('a b c d'.split())
    >>> nth(it, 2)
    'c'
    """
    return next(islice(iterable, n, None))

def pairs(iterable):
    """Get pairs of subsequent elements

    >>> list(pairs([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    """
    it1, it2 = tee(iterable)
    next(it2)
    return zip(it1, it2)

def groupn(iterable, n=2, fillvalue=None):
    """Yield non-overlapping length-n groups

    >>> list(groupn('a b c d e f g'.split(), n=3, fillvalue=None))
    [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', None, None)]
    """
    # Note: This is intentionally the same iterator repeated n times.
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def diffs(iterable):
    """Get the change from each number in the iterable to the next

    >>> list(diffs([21, 25, 19, 7, 6]))
    [4, -6, -12, -1]
    """
    return (b - a for a, b in pairs(iterable))

def quantify(iterable, pred=bool):
    """Count how many times the predicate is true

    >>> quantify([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], lambda x: x % 3 == 0)
    4
    """
    return sum(map(pred, iterable))

def ints(string):
    """Iterate over the integers present in the string

    >>> list(ints("12, 34, 56.78-9 10: 11, -12, 0123"))
    [12, 34, 56, 78, -9, 10, 11, -12, 123]
    """
    return map(int, re.findall(r"-?[0-9]+", string))

def positive_ints(string):
    """Iterate over the positive integers present in the string

    >>> list(positive_ints("12, 34, 56.78-9 10: 11, -12, 0123"))
    [12, 34, 56, 78, 9, 10, 11, 12, 123]
    """
    return map(int, re.findall(r"[0-9]+", string))

def floats(string):
    """Iterate over the floats present in the string

    >>> list(floats("123.456, .123, .0, 0., 123., 123, 0, -123, -.123"))
    [123.456, 0.123, 0.0, 0.0, 123.0, 123.0, 0.0, -123.0, -0.123]
    """
    pattern = re.compile(r"""
            -?  [0-9]+  \.   [0-9]*
        |   -?          \.   [0-9]+
        |   -?  [0-9]+
    """, re.VERBOSE)
    return map(float, pattern.findall(string))

def containsany(container_or_iterable, items):
    """Determine if the container contains any of the items.

    >>>
    """
    if hasattr(container_or_iterable, '__contains__'):
        return any(
            item in container_or_iterable
            for item in items
        )
    return bool(set(items) & set(container_or_iterable))

def containsall(container_or_iterable, items):
    """
    """
    if hasattr(container_or_iterable, '__contains__'):
        return all(
            item in container_or_iterable
            for item in items
        )
    return set(items) <= set(container_or_iterable)

def floodfill(start, successor_fn):
    region = {start}
    frontier = [start]
    while frontier:
        node = frontier.pop()
        newnodes = set(successor_fn(node)) - region
        frontier.extend(newnodes)
        region |= newnodes
    return region

def shunting_yard(rawinput, operators):
    ...

if __name__ == '__main__':
    import doctest
    doctest.testmod()

