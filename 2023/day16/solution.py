from collections import defaultdict, deque


def part_1(mat, i, j, dirx):
    n, m = len(mat), len(mat[0])
    vis = set()
    energized = set()
    q = deque([(i, j, dirx)])

    while q:
        i, j, dirx = q.popleft()
        if (i, j, dirx) in vis:
            continue
        vis.add((i, j, dirx))
        energized.add((i, j))
        if mat[i][j] == ".":
            if dirx == 0:
                if j + 1 < m:
                    q.append((i, j + 1, 0))
            elif dirx == 1:
                if i + 1 < n:
                    q.append((i + 1, j, 1))
            elif dirx == 2:
                if 0 <= j - 1:
                    q.append((i, j - 1, 2))
            else:
                if 0 <= i - 1:
                    q.append((i - 1, j, 3))

        elif mat[i][j] == "|":
            if dirx == 0 or dirx == 2:
                if i + 1 < n:
                    q.append((i + 1, j, 1))
                if 0 <= i - 1:
                    q.append((i - 1, j, 3))
            elif dirx == 1:
                if i + 1 < n:
                    q.append((i + 1, j, dirx))
            else:
                if 0 <= i - 1:
                    q.append((i - 1, j, dirx))
        elif mat[i][j] == "-":
            if dirx == 1 or dirx == 3:
                if j + 1 < m:
                    q.append((i, j + 1, 0))
                if 0 <= j - 1:
                    q.append((i, j - 1, 2))
            elif dirx == 0:
                if j + 1 < m:
                    q.append((i, j + 1, dirx))
            else:
                if 0 <= j - 1:
                    q.append((i, j - 1, dirx))
        elif mat[i][j] == "\\":
            if dirx == 0:
                if i + 1 < n:
                    q.append((i + 1, j, 1))
            elif dirx == 1:
                if j + 1 < m:
                    q.append((i, j + 1, 0))
            elif dirx == 2:
                if 0 <= i - 1:
                    q.append((i - 1, j, 3))
            else:
                if 0 <= j - 1:
                    q.append((i, j - 1, 2))
        elif mat[i][j] == "/":
            if dirx == 0:
                if 0 <= i - 1:
                    q.append((i - 1, j, 3))
            elif dirx == 1:
                if 0 <= j - 1:
                    q.append((i, j - 1, 2))
            elif dirx == 2:
                if i + 1 < n:
                    q.append((i + 1, j, 1))
            else:
                if j + 1 < m:
                    q.append((i, j + 1, 0))

    return len(energized)


def part_2(mat):
    n, m = len(mat), len(mat[0])
    max_val = 0
    for i in range(n):
        max_val = max(max_val, part_1(data, i, 0, 0))
        max_val = max(max_val, part_1(data, i, 0, 2))
    for i in range(m):
        max_val = max(max_val, part_1(data, 0, i, 1))
        max_val = max(max_val, part_1(data, 0, i, 3))
    return max_val


with open("test.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [list(d) for d in data]
    print(part_1(data, 0, 0, 0))
    print(part_2(data))
