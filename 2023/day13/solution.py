from collections import defaultdict, deque


def find_mirror(pattern, prev_r=None, prev_c=None):
    rows, cols = len(pattern), len(pattern[0])
    start = 0
    r, c = None, None
    while start < rows - 1:
        up = start
        down = start + 1
        matched = True
        while up >= 0 and down < rows:
            if pattern[up] == pattern[down]:
                up -= 1
                down += 1
            else:
                matched = False
                break
        start += 1
        if matched and prev_r != start:
            r = start
            break

    if r:
        return (r, None)
    start = 0
    while start < cols - 1:
        up = start
        down = start + 1
        matched = True
        while up >= 0 and down < cols:
            i = 0
            while i < rows and pattern[i][up] == pattern[i][down]:
                i += 1
            if i == rows:
                up -= 1
                down += 1
            else:
                matched = False
                break
        start += 1
        if matched:
            if prev_c == start:
                continue
            c = start
            break

    return (None, c)


def part_1(patterns):
    ans = []
    for pattern in patterns:
        ans.append(find_mirror(pattern))
    return ans


with open("input.txt", "r") as f:
    data = f.read().split("\n")
    patterns, curr = [], []
    for d in data:
        if len(d.strip()) == 0:
            patterns.append(curr)
            curr = []
            continue
        curr.append(list(d))

    r, c = zip(*part_1(patterns))
    print(sum([a for a in r if a]) * 100 + sum([a for a in c if a]))
    # brute force part 2
    r2, c2 = [], []
    for k, pattern in enumerate(patterns):
        found = False
        for i in range(len(pattern)):
            if found:
                break
            for j in range(len(pattern[0])):
                orig = pattern[i][j]
                pattern[i][j] = "." if pattern[i][j] == "#" else "#"
                ans = find_mirror(pattern, r[k], c[k])
                pattern[i][j] = orig
                if (ans[0], ans[1]) != (None, None):
                    r2.append(ans[0])
                    c2.append(ans[1])
                    found = True
                    break
    print(sum([a for a in r2 if a]) * 100 + sum([a for a in c2 if a]))
