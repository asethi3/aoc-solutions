from collections import defaultdict

def winners(card):
  numbers = card.split(':')[1].strip().split(' | ')
  win = set(numbers[0].strip().split())
  curr = set(numbers[1].strip().split())
  return len(win.intersection(curr))

def part_1(cards):
  return sum([2**(intersection-1) for card in cards if (intersection := winners(card))])

def part_2(cards):
  ans = 0
  counts = defaultdict(int)
  for i, card in enumerate(cards):
    counts.update({i + 1 + k: counts[i+1+k] + counts[i + 1] + 1 for k in range(1, winners(card) + 1)})
    ans += counts[i+1] + 1
  return ans

with open('input.txt', 'r') as f:
  data = f.read().strip().split('\n')
  print(part_1(data))
  print(part_2(data))
