from functools import cache

memo = {}


def dp(target, nums):
    nums_tuple = tuple(nums)
    key = (target, nums_tuple)

    if key in memo:
        return memo[key]

    if len(nums) == 0:
        if "#" not in target:
            memo[key] = 1
            return 1
        memo[key] = 0
        return 0

    if len(target) == 0:
        memo[key] = 0
        return 0
    ways = 0
    if target[0] == ".":
        ways += dp(target[1:], nums)

    elif target[0] == "#":
        if (
            "." not in target[: nums[0]]
            and nums[0] <= len(target)
            and (nums[0] == len(target) or target[nums[0]] != "#")
        ):
            ways += dp(target[nums[0] + 1 :], nums[1:])

    else:
        ways += dp(target[1:], nums)
        if (
            "." not in target[: nums[0]]
            and nums[0] <= len(target)
            and (nums[0] == len(target) or target[nums[0]] != "#")
        ):
            ways += dp(target[nums[0] + 1 :], nums[1:])
    memo[key] = ways
    return ways


def part_1(data):
    ways = 0
    for s, nums in data:
        ways += dp(s, nums)

    return ways


def part_2(data):
    ways = 0
    i = 0
    for s, nums in data:
        i += 1
        s = "?".join([s] * 5)
        nums = nums * 5
        ways += dp(s, nums)
    return ways


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    data = [(d.split()[0], [int(c) for c in d.split()[1].split(",")]) for d in data]

    print(part_1(data))
    print(part_2(data))
