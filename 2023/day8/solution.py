from collections import Counter
import math
from functools import reduce, cmp_to_key


def util(curr, instr, g):
    step = 0
    while True:
        for dirx in instr:
            curr = g[curr][0] if dirx == "L" else g[curr][1]
            step += 1
            if curr[2] == "Z":
                return step
    return -1


def part_1(data):
    instr = data[0]
    g = {d[:3]: (d[7:10], d[12:15]) for d in data[2:]}
    curr = "AAA"
    step = 0
    while True:
        for dirx in instr:
            curr = g[curr][0] if dirx == "L" else g[curr][1]
            step += 1
            if curr == "ZZZ":
                return step
    return -1


def part_2(data):
    instr = data[0]
    g = {d[:3]: (d[7:10], d[12:15]) for d in data[2:]}
    curr = [k for k in g if k[2] == "A"]
    steps = [util(c, instr, g) for c in curr]
    return math.lcm(*steps)


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    print(part_1(data))
    print(part_2(data))
