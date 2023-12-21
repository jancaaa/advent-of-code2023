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


def get_s(entries: List[List[str]]) -> Tuple[int, int]:
    for y in range(len(entries)):
        for x in range(len(entries[y])):
            if entries[y][x] == "S":
                return x, y


def get_s_next(entries: List[List[str]], s: Tuple[int, int]) -> Tuple[int, int]:
    x, y = s
    if y != 0 and entries[y - 1][x] != ".":  # N
        return x, y - 1
    elif entries[y + 1][x] != ".":  # S
        return x, y + 1
    elif x != 0 and entries[y][x - 1] != ".":  # W
        return x - 1, y
    elif entries[y][x + 1] != ".":  # E
        return x + 1, y


def get_next(entries: List[List[str]], n: Tuple[int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    x, y = n
    c = entries[y][x]
    if c == "|":
        return (x, y - 1), (x, y + 1)
    elif c == "-":
        return (x - 1, y), (x + 1, y)
    elif c == "L":
        return (x, y - 1), (x + 1, y)
    elif c == "J":
        return (x, y - 1), (x - 1, y)
    elif c == "7":
        return (x - 1, y), (x, y + 1)
    elif c == "F":
        return (x + 1, y), (x, y + 1)


def get_loop(entries: List[List[str]]) -> List[Tuple[int, int]]:
    s = get_s(entries)
    n = get_s_next(entries, s)
    loop = [s, n]
    x, y = n
    while entries[y][x] != "S":
        n1, n2 = get_next(entries, n)
        if n1 != loop[-2]:
            n = n1
        else:
            n = n2
        loop.append(n)
        x, y = n
    return loop


def part1(entries: list) -> int:
    loop = get_loop(entries)
    if len(loop) % 2 == 0:
        return len(loop) // 2
    else:
        return (len(loop) - 1) // 2


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
