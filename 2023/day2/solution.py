from collections import defaultdict
from functools import reduce

limits = {'red': 12, 'green': 13, 'blue': 14}

def is_draw_ok(s):
  count = int(s.split()[0])
  return not any([c in s and count > limits[c] for c in limits])

def part_1(lines):
  count = 0
  for i, line in enumerate(lines):
    sets = line.split(':')[1].split(';')
    if all([all([is_draw_ok(s.strip()) for s in set.split(',')]) for set in sets]):
      count += i+1
  return count

def get_counts(set):
    counts = {s.split()[1]: int(s.split()[0]) for s in set.split(',') if s.split()[1] in limits}
    return counts.get('red', 0), counts.get('green', 0), counts.get('blue', 0)

def part_2(lines):
  power_sum = 0
  for line in lines:
    sets = line.split(':')[1].split(';')
    max_r, max_b, max_g = 0, 0, 0
    for set in sets:
      r, g, b = get_counts(set)
      max_r, max_b, max_g = max(max_r, r), max(max_g, g), max(max_b, b)
    power_sum += max_r * max_g * max_b
  return power_sum

with open('input.txt', 'r') as f:
  lines = f.readlines()
  print(part_1(lines))
  print(part_2(lines))
