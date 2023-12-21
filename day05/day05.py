def read_file():
    with open("input.txt") as fp:
        line = fp.readline()
        line = line.rstrip()
        _, seeds = line.split(": ")
        fp.readline()  # empty line
        fp.readline()  # name
        line = fp.readline()
        maps = dict()
        m = []
        map_index = 0
        while line:
            line = line.rstrip()
            if line == "":
                # divider
                maps[map_index] = m
                map_index += 1
                fp.readline()  # name
                m = []
            else:
                m.append(line)
            line = fp.readline()
        maps[map_index] = m
        almanac = Almanac(seeds, maps)
    return almanac


class Almanac:
    def __init__(self, seeds: str, maps: dict):
        seeds = seeds.split(" ")
        self.seeds = [int(s) for s in seeds]
        self.maps = maps


def convert(seed: int, maps: dict) -> int:
    for m in maps.values():
        converted = None
        index = 0
        while converted is None and index < len(m):
            line = m[index]
            dest, source, l = line.split(" ")
            dest = int(dest)
            source = int(source)
            l = int(l)
            if source <= seed <= source + l - 1:
                offset = seed - source
                converted = dest + offset
            index += 1
        if converted is None:
            converted = seed
        seed = converted
    return converted


def part1(almanac: Almanac) -> int:
    converted = []
    for s in almanac.seeds:
        c = convert(s, almanac.maps)
        converted.append(c)
    return min(converted)


def part2(almanac: Almanac) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
