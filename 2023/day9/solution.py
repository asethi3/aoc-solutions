import operator


def part_1(data):
    total = 0
    for arr in data:
        last = [arr[-1]]
        while not all(i == arr[0] for i in arr):
            arr = list(map(operator.sub, arr[1:], arr[:-1]))
            last.append(arr[-1])
        next_num = last.pop()
        while last:
            next_num += last.pop()
        total += next_num
    return total


def part_2(data):
    return part_1(list(map(lambda x: x[::-1], data)))


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = list(map(lambda x: list(map(lambda y: int(y), x.split())), data))
    print(part_1(data))
    print(part_2(data))
