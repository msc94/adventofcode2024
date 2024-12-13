from utils.input import read_lines

lines = read_lines("day02.txt")

def get_differences(values):
    return [y - x for (x, y) in zip(values, values[1:])]

def is_safe(values):
    diffs = get_differences(values)
    all_increasing = all([x < 0 and x > -4 for x in diffs])
    all_decreasing = all([x > 0 and x < 4 for x in diffs])
    return all_increasing or all_decreasing

def get_lists_with_one_element_removed(original_list):
    result = []
    for i in range(len(original_list)):
        new_list = original_list[:i] + original_list[i+1:]
        result.append(new_list)
    return result


def part01():
    safe = 0
    for l in lines:
        levels = [int(x) for x in l.split()]
        safe = safe + 1 if is_safe(levels) else 0
    print(safe)

part01()
 
def part02():
    safe = 0
    for l in lines:
        levels = [int(x) for x in l.split()]
        if any([is_safe(x) for x in get_lists_with_one_element_removed(levels)]):
            safe = safe + 1 
    print(safe)

part02()

