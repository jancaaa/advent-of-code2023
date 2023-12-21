from typing import List


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            springs, counts = line.split(" ")
            counts = [int(x) for x in counts.split(",")]
            entries.append((springs, counts))
            line = fp.readline()
        return entries


def generate_strings(string: str) -> List[str]:
    generated_strings = [string]
    for i in range(len(string)):
        new_generated_strings = []
        for s in generated_strings:
            x = list(s)
            if x[i] == "?":
                x[i] = "."
                new_generated_strings.append("".join(x))
                x = list(s)
                x[i] = "#"
                new_generated_strings.append("".join(x))
                generated_strings = new_generated_strings
    return generated_strings


def part1(entries: list) -> int:
    count = 0
    for e in entries:
        spring, counts = e

        generated_strings = generate_strings(spring)
        valid_strings = []
        for s in generated_strings:
            parts = s.split(".")
            parts = [x for x in parts if x != ""]
            if parts == [c * "#" for c in counts]:
                valid_strings.append(s)
        count += len(valid_strings)
    return count


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
