from utils.input import read_lines

input = read_lines("day07.txt")
print(input)


def parse(line):
    parts_1 = line.split(":")
    goal = int(parts_1[0])
    ints = [int(x) for x in parts_1[1].split()]
    return goal, ints


def possible_combinations(goal, ints):
    if len(ints) == 1:
        if ints[0] <= goal:
            return ints
        else:
            return []

    combinations = []
    current = ints[0]

    for comb in possible_combinations(goal, ints[1:]):
        if current + comb <= goal:
            combinations.append(current + comb)
        if current * comb <= goal:
            combinations.append(current * comb)

    return combinations


def solve(goal, ints):
    ints = list(reversed(ints))
    combinations = possible_combinations(goal, ints)
    return any([x == goal for x in combinations])


def part01():
    count = 0
    for l in input:
        goal, ints = parse(l)
        if solve(goal, ints):
            count = count + goal
    print(count)


part01()
