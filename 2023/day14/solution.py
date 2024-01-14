import copy


def move_north(data):
    n, m = len(data), len(data[0])
    for j in range(m):
        pos = 0
        for i in range(n):
            if data[i][j] == "O":
                data[pos][j], data[i][j] = data[i][j], data[pos][j]
                pos += 1
            elif data[i][j] == "#":
                pos = i + 1


def move_west(data):
    n, m = len(data), len(data[0])
    for i in range(n):
        pos = 0
        for j in range(m):
            if data[i][j] == "O":
                data[i][pos], data[i][j] = data[i][j], data[i][pos]
                pos += 1
            elif data[i][j] == "#":
                pos = j + 1
    return data


def move_south(data):
    n, m = len(data), len(data[0])
    for j in range(m):
        pos = n - 1
        for i in reversed(range(n)):
            if data[i][j] == "O":
                data[pos][j], data[i][j] = data[i][j], data[pos][j]
                pos -= 1
            elif data[i][j] == "#":
                pos = i - 1
    return data


def move_east(data):
    n, m = len(data), len(data[0])
    for i in range(n):
        pos = m - 1
        for j in reversed(range(m)):
            if data[i][j] == "O":
                data[i][pos], data[i][j] = data[i][j], data[i][pos]
                pos -= 1
            elif data[i][j] == "#":
                pos = j - 1
    return data


def part_1(data):
    move_north(data)
    return calc(data)


def calc(data):
    n, m = len(data), len(data[0])
    total = 0
    for j in range(m):
        for i in range(n):
            if data[i][j] == "O":
                total += n - i
    return total


def cycle(data):
    move_north(data)
    move_west(data)
    move_south(data)
    move_east(data)
    return data


def part_2(data):
    memo = {}
    og = copy.deepcopy(data)
    cycle_length = None
    offset = None
    for i in range(1000000000):
        data = cycle(data)
        key = tuple(tuple(d) for d in data)
        if key in memo:
            offset = memo[key]
            cycle_length = i - memo[key]
            break
        memo[key] = i

    data = og
    end = offset + (1000000000 - offset) % cycle_length
    for i in range(end):
        data = cycle(data)
    return calc(data)


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [list(d) for d in data]
    print(part_1(data))
    print(part_2(data))
