from utils.input import read_lines

input = read_lines("day04.txt")
width = len(input[0])
height = len(input)


def get(input, x, y):
    if x < 0 or x >= width:
        return None
    if y < 0 or y >= height:
        return None
    return input[x][y]


def do_count(input, x, y):
    xmas = "XMAS"

    count = 0

    # Horizontal
    if all([get(input, x + d, y) == xmas[d] for d in range(4)]):
        count = count + 1

    if all([get(input, x + 3 - d, y) == xmas[d] for d in range(4)]):
        count = count + 1

    # Vertical
    if all([get(input, x, y + d) == xmas[d] for d in range(4)]):
        count = count + 1

    if all([get(input, x, y + 3 - d) == xmas[d] for d in range(4)]):
        count = count + 1

    # Top left to bottom right
    if all([get(input, x + d, y + d) == xmas[d] for d in range(4)]):
        count = count + 1

    if all([get(input, x + 3 - d, y + 3 - d) == xmas[d] for d in range(4)]):
        count = count + 1

    # Top right to bottom left
    if all([get(input, x + 3 - d, y + d) == xmas[d] for d in range(4)]):
        count = count + 1

    if all([get(input, x + d, y + 3 - d) == xmas[d] for d in range(4)]):
        count = count + 1

    return count


def part01():
    count = 0

    for y in range(height):
        for x in range(width):
            count = count + do_count(input, x, y)

    print(count)


part01()
