from utils.input import read_lines

lines = read_lines("day01.txt")

first = []
second = []

for line in lines:
    parts = line.split()
    first.append(int(parts[0]))
    second.append(int(parts[1]))

def part01():
    first.sort()
    second.sort()

    result = 0

    for (x, y) in zip(first, second):
        result = result + abs(x - y)

    print(result)

def part02():
    frequency = dict()
    for i in second:
        frequency[i] = frequency.setdefault(i, 0) + 1

    result = 0
    for i in first:
        result = result + i * frequency.setdefault(i, 0)

    print(result)

part02()
