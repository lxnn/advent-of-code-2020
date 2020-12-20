import sys, collections, re

if len(sys.argv) == 2:
    with open(sys.argv[1]) as file:
        raw = file.read()
else:
    raw = sys.stdin.read()

class Int(int):
    def __add__(self, other):   return Int(int(self) + int(other))
    def __and__(self, other):   return Int(int(self) * int(other))
    __radd__ = __add__
    __rand__ = __and__

print(sum(
    eval(re.sub(r"(\d+)", r"Int(\1)", re.sub(r"\*", r"&", expression)))
    for expression in raw.splitlines()
))
