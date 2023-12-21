from typing import Tuple


def read_file() -> list:
    with open("input.txt") as fp:
        time = fp.readline().rstrip()
        _, time = time.split(":")
        distance = fp.readline().rstrip()
        _, distance = distance.split(":")
        return time, distance


def read_file1() -> list:
    with open("input.txt") as fp:
        time = fp.readline().rstrip()
        _, time = time.split(":")
        time = time.split()
        distance = fp.readline().rstrip()
        _, distance = distance.split(":")
        distance = distance.split()
        entries = []
        for i in range(len(time)):
            r_t = time[i]
            r_d = distance[i]
            race = (int(r_t), int(r_d))
            entries.append(race)
        return entries


def read_file2() -> Tuple[int, int]:
    with open("input.txt") as fp:
        time = fp.readline().rstrip()
        _, time = time.split(":")
        time = time.replace(" ", "")
        time = int(time)

        distance = fp.readline().rstrip()
        _, distance = distance.split(":")
        distance = distance.replace(" ", "")
        distance = int(distance)
        return time, distance


def part1(time, distance) -> int:
    time = time.split()
    distance = distance.split()
    races = []
    for i in range(len(time)):
        r_t = time[i]
        r_d = distance[i]
        race = (int(r_t), int(r_d))
        races.append(race)

    result = 1
    for race in races:
        options = 0
        time, distance = race
        for i in range(1, time):
            t = time - i
            d = t * i
            if d > distance:
                options += 1
        result *= options

    return result


def part2(time, distance) -> int:
    time = time.replace(" ", "")
    time = int(time)

    distance = distance.replace(" ", "")
    distance = int(distance)

    options = 0
    for i in range(1, time):
        if (time - i) * i > distance:
            options += 1
    return options


if __name__ == "__main__":
    entries = read_file1()
    time, distance = read_file()
    print(f"Part 1: {part1(time, distance)}")
    print(f"Part 2: {part2(time, distance)}")
