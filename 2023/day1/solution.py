digits = ['zero', 'one', 'two', 'three',
          'four', 'five', 'six',
          'seven', 'eight', 'nine']


def part_1(s):
    first = s[[c.isdigit() for c in s].index(True)]
    last = s[-[c.isdigit() for c in reversed(s)].index(True)-1]
    return int(first + last)


def part_2(s):
    first, last = None, None
    for i in range(len(s)):
        digit = None
        if s[i].isdigit():
            digit = int(s[i])
        else:
            digits_found = [s[i:].startswith(word) for word in digits]
            matches = [idx for idx, b in enumerate(digits_found) if b]
            if matches:
                digit = matches[0]
        if digit:
            if not first:
                first = digit
            last = digit
    return first*10 + last


with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')
    print(sum([part_1(d) for d in data]))
    print(sum([part_2(d) for d in data]))
