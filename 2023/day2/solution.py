colors = {'red': 12, 'green': 13, 'blue': 14}


def is_draw_ok(s):
    count = int(s.split()[0])
    return not any([c in s and count > colors[c] for c in colors])


def part_1(games):
    count = 0
    for i, game in enumerate(games):
        sets = game.split(':')[1].split(';')
        if all([all([is_draw_ok(s.strip()) for s in set.split(',')]) for set in sets]):
            count += i+1
    return count


def get_counts(set):
    counts = {s.split()[1]: int(s.split()[0])
              for s in set.split(',') if s.split()[1] in colors}
    return counts.get('red', 0), counts.get('green', 0), counts.get('blue', 0)


def part_2(games):
    power_sum = 0
    for game in games:
        sets = game.split(':')[1].split(';')
        max_r, max_b, max_g = 0, 0, 0
        for set in sets:
            r, g, b = get_counts(set)
            max_r, max_b, max_g = max(max_r, r), max(max_g, g), max(max_b, b)
        power_sum += max_r * max_g * max_b
    return power_sum


with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')
    print(part_1(data))
    print(part_2(data))
