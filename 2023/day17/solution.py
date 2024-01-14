from collections import defaultdict, deque
import heapq
import math


def part_1(mat):
    n, m = len(mat), len(mat[0])
    dist = defaultdict(lambda: float("inf"))
    q = []
    heapq.heappush(q, (0, 0, 0, 0, 0))
    heapq.heappush(q, (0, 0, 0, 1, 0))
    min_heat = math.inf
    while q:
        d, i, j, prev_dir, count = heapq.heappop(q)

        if i == n - 1 and j == m - 1:
            min_heat = min(min_heat, d)
            continue

        for dx, dy, dirx in [(1, 0, 1), (-1, 0, 3), (0, 1, 0), (0, -1, 2)]:
            if (
                (prev_dir == 0 and dirx == 2)
                or (prev_dir == 1 and dirx == 3)
                or (prev_dir == 2 and dirx == 0)
                or (prev_dir == 3 and dirx == 1)
            ) or (dirx == prev_dir and count == 3):
                continue
            x, y = i + dx, j + dy
            new_count = (count + 1) if dirx == prev_dir else 1

            if 0 <= x < n and 0 <= y < m:
                if d + int(mat[x][y]) < dist[(x, y, dirx, new_count)]:
                    dist[(x, y, dirx, new_count)] = d + int(mat[x][y])
                    heapq.heappush(
                        q,
                        (dist[(x, y, dirx, new_count)], x, y, dirx, new_count),
                    )
    return min_heat


def part_2(mat):
    n, m = len(mat), len(mat[0])
    dist = defaultdict(lambda: float("inf"))
    q = []
    heapq.heappush(q, (0, 0, 0, 0, 0))
    heapq.heappush(q, (0, 0, 0, 1, 0))
    min_heat = math.inf
    while q:
        d, i, j, prev_dir, count = heapq.heappop(q)

        if i == n - 1 and j == m - 1 and 4 <= count:
            min_heat = min(min_heat, d)
            continue

        for dx, dy, dirx in [(1, 0, 1), (-1, 0, 3), (0, 1, 0), (0, -1, 2)]:
            if (
                (count < 4 and dirx != prev_dir)
                or (count >= 10 and dirx == prev_dir)
                or (prev_dir == 0 and dirx == 2)
                or (prev_dir == 1 and dirx == 3)
                or (prev_dir == 2 and dirx == 0)
                or (prev_dir == 3 and dirx == 1)
            ):
                continue
            x, y = i + dx, j + dy
            new_count = (count + 1) if dirx == prev_dir else 1

            if (
                0 <= x < n
                and 0 <= y < m
                and d + int(mat[x][y]) < dist[(x, y, dirx, new_count)]
            ):
                dist[(x, y, dirx, new_count)] = d + int(mat[x][y])
                heapq.heappush(
                    q,
                    (dist[(x, y, dirx, new_count)], x, y, dirx, new_count),
                )
    return min_heat


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [list(d) for d in data]
    print(part_1(data))
    print(part_2(data))
