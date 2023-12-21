def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(list(line))
            line = fp.readline()
        return entries


def part1(entries: list) -> int:
    for y in range(1, len(entries[0])):
        for x in range(0, len(entries)):
            if entries[y][x] == "O":
                new_y = y
                while new_y > 0 and entries[new_y - 1][x] == ".":
                    new_y -= 1
                entries[y][x] = "."
                entries[new_y][x] = "O"

    sum = 0
    for i, e in enumerate(entries):
        count = e.count("O")
        sum += count * (len(entries) - i)

    return sum


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
