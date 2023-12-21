def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(Card(line))
            line = fp.readline()
        return entries


class Card:
    def __init__(self, line: str):
        id, cards = line.split(": ")
        _, id = id.split()
        win, num = cards.split(" | ")
        win = win.split()
        num = num.split()
        self.id = int(id)
        self.win = [int(n) for n in win]
        self.num = [int(n) for n in num]
        self.count = 1

    def count_winning_numbers(self) -> int:
        count = 0
        for w in self.win:
            if self.num.count(w) > 0:
                count += 1
        return count


def part1(cards: list) -> int:
    sum = 0
    for card in cards:
        c = card.count_winning_numbers()
        if c > 0:
            sum += pow(2, c - 1)
    return sum


def part2(cards: list) -> int:
    sum = 0
    for card in cards:
        c = card.count_winning_numbers()
        for i in range(c):
            cards[card.id + i].count += card.count
    for card in cards:
        sum += card.count
    return sum


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
