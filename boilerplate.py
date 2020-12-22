import sys, collections, functools, math, re, operator
from string import (ascii_lowercase as alphabet, digits)
from typing import (List, Set, Dict, NamedTuple)

try:
    with open(sys.argv[1]) as file:
        raw = file.read()
except IndexError:
    raw = sys.stdin.read()



