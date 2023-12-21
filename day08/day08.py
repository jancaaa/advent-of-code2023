def read_file() -> list:
    with open("input.txt") as fp:
        instructions = fp.readline().rstrip()
        line = fp.readline()  # empty line
        line = fp.readline()
        entries = {}
        while line:
            line = line.rstrip()
            node, instr = line.split(" = ")
            instr = instr[1:-1]
            left, right = instr.split(", ")
            entries[node] = (left, right)
            line = fp.readline()
        return instructions, entries


def part1(instructions: str, entries: dict) -> int:
    count = 0
    current = "AAA"
    while current != "ZZZ":
        left, right = entries[current]
        i = count % len(instructions)

        if instructions[i] == "L":
            current = left
        else:
            current = right
        count += 1

    return count


def part2(instructions: str, entries: dict) -> int:
    return


if __name__ == "__main__":
    instructions, entries = read_file()
    print(f"Part 1: {part1(instructions, entries)}")
    print(f"Part 2: {part2(instructions, entries)}")
