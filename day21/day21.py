from typing import Tuple, List


def read_file() -> List[List[str]]:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(list(line))
            line = fp.readline()
        return entries


def get_s(entries: List[List[str]]) -> Tuple:
    for y in range(len(entries)):
        for x in range(len(entries[y])):
            if entries[y][x] == "S":
                return x, y


def get_neighbours(c: Tuple[int, int], entries: List[List[str]]):
    n = []
    x, y = c
    if x != 0:
        n.append((x - 1, y))
    if x != len(entries[y]) - 1:
        n.append((x + 1, y))
    if y != 0:
        n.append((x, y - 1))
    if y != len(entries) - 1:
        n.append((x, y + 1))
    return n


def part1(entries: List[List[str]]) -> int:
    start = get_s(entries)
    x, y = start
    entries[y][x] = "."
    current = set()
    current.add(start)
    for _ in range(64):
        next = set()
        for c in current:
            neighbours = get_neighbours(c, entries)
            for n in neighbours:
                x, y = n
                if entries[y][x] == ".":
                    next.add(n)

        current = next
    return len(current)


def part2(entries: List[List[str]]) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
