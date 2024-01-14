def part_1(data):
    steps = data[0].split(",")
    total = 0
    for step in steps:
        curr = 0
        for c in step:
            curr = ((curr + ord(c)) * 17) % 256
        total += curr
    return total


def part_2(data):
    steps = data[0].split(",")
    buckets = [[]] * 256
    for step in steps:
        label = step.split("-")[0] if "-" in step else step.split("=")[0]
        focal = None if "-" in step else int(step.split("=")[1])
        code = 0
        for c in label:
            code = ((code + ord(c)) * 17) % 256

        if focal:
            present = False
            for i, lens in enumerate(buckets[code]):
                if lens[0] == label:
                    buckets[code][i] = (label, focal)
                    present = True
                    break
            if not present:
                buckets[code] = buckets[code] + [(label, focal)]
        else:
            for i, lens in enumerate(buckets[code]):
                if lens[0] == label:
                    buckets[code] = buckets[code][:i] + buckets[code][i + 1 :]
                    break

    total = 0
    for i, bucket in enumerate(buckets):
        for j, lens in enumerate(bucket):
            total += (i + 1) * (j + 1) * (lens[1])
    return total


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")
    print(part_1(data))
    print(part_2(data))
