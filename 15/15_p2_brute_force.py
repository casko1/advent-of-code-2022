import re
import time
from collections import defaultdict

lines = open('in.txt').read().split('\n')

range_dict = defaultdict(list)

start = time.time()

for line in lines:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r'-?\d+\.?\d*', line)]

    dist = abs(x1 - x2) + abs(y1 - y2)

    for i in range(dist):
        top_y, bottom_y = y1 - dist + i, y1 + dist - i

        from_x, to_x = min(max(x1 - i, 0), 4000000), min(max(x1 + i, 0), 4000000)

        range_tuple = [from_x, to_x]

        if 0 <= top_y <= 4000000:
            range_dict[top_y].append(range_tuple)

        if 0 <= bottom_y <= 4000000:
            range_dict[bottom_y].append(range_tuple)

    range_dict[y1].append([min(max(x1 - dist, 0), 4000000), min(max(x1 + dist, 0), 4000000)])


for k in range_dict:
    arr = range_dict[k]
    arr.sort(key=lambda interval: interval[0])
    merged = [arr[0]]
    for current in arr:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)

    if (len(merged)) == 2:
        if merged[1][0] - merged[0][1] == 2:
            print((merged[0][1] + 1) * 4000000 + k)
            break

print(f'Part 2: {time.time() - start}')
