import sys

try:
    with open(sys.argv[1]) as file:
        rawinput = file.read()
except IndexError:
    rawinput = sys.stdin.read()

expressions = map(str.strip, rawinput.splitlines())

def torpn(exp):
    stack = []
    for char in exp:
        if char in '0123456789':
            yield int(char)
            while stack and stack[-1] != '(':
                yield stack.pop()
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                yield stack.pop()
            assert stack and stack.pop() == '('
            while stack and stack[-1] != '(':
                yield stack.pop()
        elif char == '+':
            stack.append(char)
        elif char == '*':
            stack.append(char)
        else:
            continue
    assert '(' not in stack and ')' not in stack
    while stack:
        yield stack.pop()

def evalrpn(rpn):
    stack = []
    for item in rpn:
        if isinstance(item, int):
            stack.append(item)
        elif item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '*':
            stack.append(stack.pop() * stack.pop())
    assert len(stack) == 1
    return stack.pop()

def evalexp(exp):
    return evalrpn(torpn(exp))

print(sum(map(evalexp, expressions)))
