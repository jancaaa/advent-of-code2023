from collections import Counter
from typing import List


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(Cards(line))
            line = fp.readline()
        return entries


class Cards:
    def __init__(self, line: str):
        cards, bid = line.split(" ")
        self.cards = cards
        self.bid = int(bid)

    def __lt__(self, other):
        cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return cards.index(self.cards[i]) < cards.index(other.cards[i])


def part1(cards: List[Cards]) -> int:
    hand = {
        "five": [],
        "four": [],
        "full_house": [],
        "three": [],
        "two": [],
        "one": [],
        "high": []
    }
    for c in cards:
        counter = Counter(c.cards)
        if len(counter.keys()) == 1:
            hand["five"].append(c)
        elif len(counter.keys()) == 5:
            hand["high"].append(c)
        elif 4 in counter.values():
            hand["four"].append(c)
        elif 3 in counter.values():
            if 2 in counter.values():
                hand["full_house"].append(c)
            else:
                hand["three"].append(c)
        elif list(counter.values()).count(2) == 2:
            hand["two"].append(c)
        elif 2 in counter.values():
            hand["one"].append(c)

    ordered = []
    for k in hand.keys():
        ordered.extend(sorted(hand[k]))

    result = 0
    for index, hand in enumerate(reversed(ordered)):
        result += (index + 1) * hand.bid
    return result


def part2(cards: List[Cards]) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
