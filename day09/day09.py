def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            line = line.split(" ")
            entries.append([int(n) for n in line])
            line = fp.readline()
        return entries


def is_all_zero(line):
    line = set(line)
    return len(line) == 1 and 0 in line


def get_full_history(e):
    transformed = [e]
    while not is_all_zero(transformed[-1]):
        line = transformed[-1]
        next_line = []
        for i in range(len(line) - 1):
            x = line[i + 1] - line[i]
            next_line.append(x)
        transformed.append(next_line)
    return transformed


def part1(entries: list) -> int:
    sum = 0
    for e in entries:
        x = 0
        for l in reversed(e):
            x += l[-1]
        sum += x
    return sum


def part2(entries: list) -> int:
    sum = 0
    for e in entries:
        x = 0
        for l in reversed(e):
            x = l[0] - x
        sum += x
    return sum


if __name__ == "__main__":
    entries = read_file()
    detailed = []
    for e in entries:
        detailed.append(get_full_history(e))
    print(f"Part 1: {part1(detailed)}")
    print(f"Part 2: {part2(detailed)}")
