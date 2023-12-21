def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(list(line))
            line = fp.readline()
        return entries


def get_symbol_neighbours(entries: list, x: int, y: int) -> list:
    neighbours = []

    if y != 0:
        neighbours.append(entries[y - 1][x])  # N

        if x != 0:
            neighbours.append(entries[y - 1][x - 1])  # NW

        if x != len(entries[y]) - 1:
            neighbours.append(entries[y - 1][x + 1])  # NE

    if y != len(entries) - 1:
        neighbours.append(entries[y + 1][x])  # S

        if x != 0:
            neighbours.append(entries[y + 1][x - 1])  # SW

        if x != len(entries[y]) - 1:
            neighbours.append(entries[y + 1][x + 1])  # SE

    if x != 0:
        neighbours.append(entries[y][x - 1])  # W

    if x != len(entries[y]) - 1:
        neighbours.append(entries[y][x + 1])  # E

    symbols = []
    for x in range(len(neighbours)):
        a = neighbours[x]
        if a.isdigit() or a == ".":
            pass
        else:
            symbols.append(a)
    return symbols


def part1(entries: list) -> int:
    sum = 0
    for y in range(len(entries)):
        x = 0
        n = ""
        neighbours = []
        while x < len(entries[y]):
            while x < len(entries[y]) and entries[y][x].isdigit():
                n += entries[y][x]
                nn = get_symbol_neighbours(entries, x, y)
                neighbours.extend(nn)
                x += 1
            if n != "" and neighbours != []:
                sum += int(n)

            x += 1
            n = ""
            neighbours = []
    return sum


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
