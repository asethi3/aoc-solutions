def get_moves(c):
    if c == "|":
        return [(1, 0), (-1, 0)]
    if c == "-":
        return [(0, 1), (0, -1)]
    if c == "F":
        return [(0, 1), (1, 0)]
    if c == "7":
        return [(0, -1), (1, 0)]
    if c == "J":
        return [(-1, 0), (0, -1)]
    if c == "L":
        return [(-1, 0), (0, 1)]
    if c == "S":
        return [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return []


def dfs(mat, start_x, start_y):
    vis = set([(start_x, start_y)])
    stack = [(start_x, start_y)]
    n, m = len(mat), len(mat[0])
    moves = 0
    max_moves = 0
    while stack:
        i, j = stack.pop()
        for dx, dy in get_moves(mat[i][j]):
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and mat[x][y] != ".":
                if (x, y) not in vis:
                    vis.add((x, y))
                    moves += 1
                    stack.append((x, y))
                elif mat[x][y] == "S":
                    max_moves = max(moves, max_moves)
    return max_moves, vis


def part_1(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "S":
                ans, vis = dfs(mat, i, j)
    return ans // 2 if ans % 2 == 0 else ans // 2 + 1, vis


def is_internal(mat, x, y, vis):
    count = 0
    order = [mat[x][j] for j in range(y, -1, -1) if (x, j) in vis and mat[x][j] != "-"][
        ::-1
    ]
    for i in range(len(order)):
        if order[i] == "|":
            count += 1
        elif i < len(order) - 1 and order[i] == "F" and order[i + 1] == "J":
            count += 1
        elif i < len(order) - 1 and order[i] == "L" and order[i + 1] == "7":
            count += 1
    return count % 2 == 1


def part_2(mat, vis):
    return sum(
        [
            1
            for i in range(len(mat))
            for j in range(len(mat[0]))
            if (i, j) not in vis and is_internal(mat, i, j, vis)
        ]
    )


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [list(d) for d in data]
    part_1_ans, vis = part_1(data)

    print(part_1_ans)
    print(part_2(data, vis))
