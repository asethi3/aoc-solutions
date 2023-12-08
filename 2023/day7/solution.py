from collections import Counter
from functools import reduce, cmp_to_key


ref = {str(a): a for a in range(2, 10)}
ref.update({"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10})


def compare_high_card(h1, h2):
    for c1, c2 in zip(list(h1), list(h2)):
        v1, v2 = ref[c1], ref[c2]
        if v1 == v2:
            continue
        return 1 if v1 > v2 else -1
    return 0


def compare_util(h1, h2, counts1, counts2):
    conditions = [
        (counts1[5] == 1, counts2[5] == 1),
        (counts1[4] == 1, counts2[4] == 1),
        (counts1[3] == 1 and counts1[2] == 1, counts2[3] == 1 and counts2[2] == 1),
        (counts1[3] == 1, counts2[3] == 1),
        (counts1[2] == 2, counts2[2] == 2),
        (counts1[2] == 1, counts2[2] == 1),
    ]

    for c1, c2 in conditions:
        if c1 and c2:
            return compare_high_card(h1, h2)
        if c1:
            return 1
        if c2:
            return -1

    return compare_high_card(h1, h2)


def compare_hands_1(hand1, hand2):
    h1, h2 = hand1[0], hand2[0]
    counts1 = Counter(Counter(h1).values())
    counts2 = Counter(Counter(h2).values())
    return compare_util(h1, h2, counts1, counts2)


def compare_hands_2(hand1, hand2):
    h1, h2 = hand1[0], hand2[0]
    h1a, h2a = h1.replace("J", ""), h2.replace("J", "")
    f1, f2 = Counter(h1a), Counter(h2a)
    max_val_card1 = max(f1, key=f1.get) if f1 else h1a[0] if h1a else "A"
    max_val_card2 = max(f2, key=f2.get) if f2 else h2a[0] if h2a else "A"

    counts1 = Counter(Counter(h1.replace("J", max_val_card1)).values())
    counts2 = Counter(Counter(h2.replace("J", max_val_card2)).values())
    return compare_util(h1, h2, counts1, counts2)


def solver(data, comparator):
    hands = [(s.split()[0], s.split()[1]) for s in data]
    ranked = sorted(hands, key=cmp_to_key(comparator))
    return sum([(i + 1) * int(r[1]) for i, r in enumerate(ranked)])


def part_1(data):
    return solver(data, compare_hands_1)


def part_2(data):
    ref["J"] = 1
    return solver(data, compare_hands_2)


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    print(part_1(data))
    print(part_2(data))
