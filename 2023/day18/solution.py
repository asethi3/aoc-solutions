from collections import defaultdict, deque
import heapq
import math


def shoelace(points):
    points.append(points[0])
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i + 1][1] - points[i][1] * points[i + 1][0]
    return abs(area // 2) + (len(points) - 1) // 2 + 1


def get_points(data, use_hex=False):
    i, j = 0, 0
    points = [(0, 0)]
    dirs = {"R": 0, "D": 1, "L": 2, "U": 3}
    for dir, step, color in data:
        if use_hex:
            step = int("0x" + color[2:-2], 0)
            dir = int(color[-2])
        else:
            step = int(step)
            dir = dirs[dir]
        if dir == 0:
            k = 1
            while k <= step:
                points.append((i, j + k))
                k += 1
            j += step

        elif dir == 2:
            k = 1
            while k <= step:
                points.append((i, j - k))
                k += 1
            j -= step
        elif dir == 1:
            k = 1
            while k <= step:
                points.append((i + k, j))
                k += 1
            i += step
        elif dir == 3:
            k = 1
            while k <= step:
                points.append((i - k, j))
                k += 1
            i -= step
    return points


def part_1(data):
    points = get_points(data)
    return shoelace(points)


def part_2(data):
    points = get_points(data, True)
    return shoelace(points)


with open("test.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [d.split() for d in data]
    print(part_1(data))
    print(part_2(data))
