from functools import reduce


def find_range(times, dist):
    ways = [next(end - next(start for start in range(time) if (time - start) * start > dist[i]) +
                 1 for end in range(time, -1, -1) if (time - end) * end > dist[i]) for i, time in enumerate(times)]
    return reduce((lambda x, y: x * y), ways)


def part_1(data):
    times = [int(s) for s in data[0].split(':')[1].strip().split()]
    dist = [int(s) for s in data[1].split(':')[1].strip().split()]
    return find_range(times, dist)


def part_2(data):
    time = int(data[0].split(':')[1].replace(' ', ''))
    dist = int(data[1].split(':')[1].replace(' ', ''))
    return find_range([time], [dist])


with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')
    print(part_1(data))
    print(part_2(data))
