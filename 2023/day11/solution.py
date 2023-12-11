from collections import defaultdict, deque


def bfs(i, j, mat, empty_rows, empty_cols, inc):
    n, m = len(mat), len(mat[0])
    q = deque([(i, j, 0)])
    vis = set([(i, j)])
    dist = defaultdict(int)

    while q:
        i, j, d = q.popleft()
        if mat[i][j] == "#":
            if (i, j) not in dist:
                dist[(i, j)] = d

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and (x, y) not in vis:
                vis.add((x, y))
                increment = 1
                if x != i and x in empty_rows:
                    increment += inc
                if y != j and y in empty_cols:
                    increment += inc
                q.append((x, y, d + increment))
    return dist


def part_1(mat, inc=1):
    n, m = len(mat), len(mat[0])
    empty_rows = [i for i in range(n) if all(mat[i][j] == "." for j in range(m))]
    empty_cols = [i for i in range(m) if all(mat[j][i] == "." for j in range(n))]
    total = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "#":
                dist = bfs(i, j, mat, empty_rows, empty_cols, inc)
                total += sum(dist.values())
    return total // 2


def part_2(mat):
    return part_1(mat, 1000000 - 1)


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [list(d) for d in data]

    print(part_1(data))
    print(part_2(data))
