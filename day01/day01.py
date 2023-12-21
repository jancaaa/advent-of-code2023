def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(line)
            line = fp.readline()
        return entries


def extract_numbers(s: str) -> int:
    numbers = []
    for char in s:
        if char.isdigit():
            numbers.append(char)
    numbers = numbers[0] + numbers[-1]
    return int(numbers)


def replace_string_digit(s: str) -> str:
    s = s.replace("one", "o1e")
    s = s.replace("two", "t2o")
    s = s.replace("three", "th3ee")
    s = s.replace("four", "f4r")
    s = s.replace("five", "f5e")
    s = s.replace("six", "s6x")
    s = s.replace("seven", "se7en")
    s = s.replace("eight", "ei8ht")
    s = s.replace("nine", "n9e")
    return s


def part1(entries: list) -> int:
    sum = 0
    for e in entries:
        n = extract_numbers(e)
        sum += n
    return sum


def part2(entries: list) -> int:
    sum = 0
    for e in entries:
        e = replace_string_digit(e)
        n = extract_numbers(e)
        sum += n
    return sum


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
