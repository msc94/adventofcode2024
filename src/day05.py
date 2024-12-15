import bisect
import re
import functools

from utils.input import read_lines

input = read_lines("day05.txt")

def parse_input(input):
    rules = []
    updates = None

    for l in input:
        if not l:
            updates = []
        elif updates is None:
            parts = l.split('|')
            rules.append((int(parts[0]), int(parts[1])))
        else:
            parts = [int(x) for x in l.split(',')]
            updates.append(parts)

    return rules, updates

rules, updates = parse_input(input)

def compare(a, b):
    for r in rules:
        if r[0] == a and r[1] == b:
            return -1
        elif r[0] == b and r[1] == a:
            return 1
    raise RuntimeError(f"No rule for {a}|{b}")


def get_middle(u):
    assert(len(u) % 2 == 1)
    return u[len(u) // 2]


def part01():
    count = 0

    for u in updates:
        s = sorted(u, key=functools.cmp_to_key(compare))
        if s == u:
            middle = get_middle(u)
            count = count + middle

    print(count)



part01()

