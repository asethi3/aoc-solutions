from collections import Counter, deque
from itertools import chain
import re


def find_gear_parts(mat, i, j):
    parts = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x, y = i + dx, j + dy
        if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and re.match('[0-9]', mat[x][y]):
            l, r = y, y + 1
            while 0 <= l and re.match('[0-9]', mat[x][l]):
                l -= 1
            while r < len(mat) and re.match('[0-9]', mat[x][r]):
                r += 1
            if l+1 != r:
                parts.append(int("".join(mat[x][l+1:r])))
                for k in range(l+1, r):
                    mat[x][k] = '.'
    return parts


def part_1(mat):
    ans = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if not re.match('[0-9\.]', mat[i][j]):
                ans += sum(find_gear_parts(mat, i, j))
    return ans


def part_2(mat):
    ans = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '*':
                nums = find_gear_parts(mat, i, j)
                if len(nums) == 2:
                    ans += nums[0]*nums[1]
    return ans


with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')
    print(part_1([list(s) for s in data]))
    print(part_2([list(s) for s in data]))
