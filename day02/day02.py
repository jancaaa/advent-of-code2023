def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(Game(line))
            line = fp.readline()
        return entries


class Game:
    def __init__(self, line):
        game, draws = line.split(": ")
        _, game_id = game.split(" ")
        draws = draws.split("; ")
        parsed_draws = []
        for draw in draws:
            draw = draw.split(", ")
            parsed_draw = []
            for x in draw:
                count, color = x.split(" ")
                parsed_draw.append((int(count), color))
            parsed_draws.append(parsed_draw)

        self.game_id = int(game_id)
        self.draws = parsed_draws


def part1(entries: list) -> int:
    sum = 0
    content = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for e in entries:
        is_possible = True
        for draw in e.draws:
            for x in draw:
                count, color = x
                if content[color] < count:
                    is_possible = False
        if is_possible:
            sum += e.game_id
    return sum


def part2(entries: list) -> int:
    sum = 0
    for e in entries:
        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for draw in e.draws:
            for x in draw:
                count, color = x
                if minimums[color] < count:
                    minimums[color] = count
        sum += minimums["red"] * minimums["green"] * minimums["blue"]

    return sum


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
