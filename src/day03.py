import bisect
import re

from utils.input import read_input

input = read_input("day03.txt")
# input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def part01():
    regex = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for match in regex.findall(input):
        (x, y) = match
        result = result + int(x) * int(y)
    print(result)


part01()


def is_enabled(pos, disabled, enabled):
    disabled_position = bisect.bisect(disabled, pos)
    enabled_position = bisect.bisect(enabled, pos)

    if disabled_position == 0:
        return True

    if enabled_position == 0:
        return False

    next_smaller_disabled = disabled[disabled_position - 1]
    next_smaller_enabled = enabled[enabled_position - 1]

    return next_smaller_enabled > next_smaller_disabled


def part02():
    disabled = [x.end() for x in re.finditer("don't\(\)", input)]
    enabled = [x.end() for x in re.finditer("do\(\)", input)]

    result = 0
    for match in re.finditer("mul\((\d{1,3}),(\d{1,3})\)", input):
        text = match.group()
        pos = match.start()
        active = is_enabled(pos, disabled, enabled)
        if active:
            result = result + int(match.group(1)) * int(match.group(2))

    print(result)


part02()
