from utils.input import read_lines

input = read_lines("day06.txt")


class Map:
    def parse_input(self, input):
        self.height = len(input)
        self.width = len(input[0])
        self.map = []
        self.visited = set()
        self.over = False

        for y in range(self.height):
            self.map.append([])
            for x in range(self.width):
                c = input[y][x]
                self.map[y].append(c)
                if c in ("<", ">", "^", "v"):
                    self.x = x
                    self.y = y

        self.visited.add((self.x, self.y))

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(f"{self.map[y][x]}", end="")
            print()
        print()

    def step(self):
        # Get next position
        current_direction = self.map[self.y][self.x]
        self.map[self.y][self.x] = "."

        if current_direction == "^":
            (new_x, new_y) = (self.x, self.y - 1)
            new_direction = ">"
        elif current_direction == "v":
            (new_x, new_y) = (self.x, self.y + 1)
            new_direction = "<"
        elif current_direction == "<":
            (new_x, new_y) = (self.x - 1, self.y)
            new_direction = "^"
        elif current_direction == ">":
            (new_x, new_y) = (self.x + 1, self.y)
            new_direction = "v"
        else:
            assert False

        if new_x < 0 or new_y < 0 or new_x >= self.width or new_y >= self.height:
            self.over = True
            return

        if self.map[new_y][new_x] == "#":
            self.map[self.y][self.x] = new_direction
        else:
            (self.x, self.y) = (new_x, new_y)
            self.visited.add((self.x, self.y))
            self.map[self.y][self.x] = current_direction


map = Map()
map.parse_input(input)
map.print()


def part01():
    while not map.over:
        map.step()
    print(len(map.visited))


part01()
