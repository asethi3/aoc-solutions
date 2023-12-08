from collections import defaultdict
import math
import re


def build_range(lines, reverse):
    range = []
    for l in lines:
        if l.strip():
            source, dest, length = [int(s) for s in l.split()]
            range.append((source, dest, length) if reverse else (dest, source, length))

    return range


def build_ranges(data, reverse=False):
    ranges = []
    i = 0
    while i < len(data):
        if "map" in data[i]:
            j = i + 1
            while j < len(data) and "map" not in data[j]:
                j += 1
            ranges.append(build_range(data[i + 1 : j], reverse))
            i = j - 1
        i += 1
    return ranges


def part_1(data):
    seeds = [int(s) for s in data[0].split(":")[1].strip().split()]
    ranges = build_ranges(data)
    ans = math.inf
    for seed in seeds:
        val = seed
        for i, range in enumerate(ranges):
            for s, d, l in range:
                if s <= seed < s + l:
                    val = d + seed - s
                    break
            seed = val
        ans = min(ans, val)
    return ans


def part_2(data):
    vals = [int(s) for s in data[0].split(":")[1].strip().split()]
    seed_ranges = [(vals[i], vals[i] + vals[i + 1]) for i in range(0, len(vals), 2)]
    ranges = build_ranges(data, True)
    ans = math.inf

    for seed in range(int(5e7), int(1e10)):
        curr = seed
        val = curr
        for r in ranges[::-1]:
            for s, d, l in r:
                if s <= curr < s + l:
                    val = d + curr - s
                    break
            curr = val
        for s, d in seed_ranges:
            if s <= val < d:
                return seed
    return -1


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    print(part_1(data))
    print(part_2(data))
