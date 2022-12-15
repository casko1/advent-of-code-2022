import re
from copy import deepcopy

lines = open('in.txt').read().split('\n')

blocked = set()

max_y = -1

for line in lines:
    nums = re.findall(r'\d+', line)

    for i in range(0, len(nums) - 2, 2):
        x1, y1, x2, y2 = nums[i:i + 4]
        if x1 == x2:
            t = max(int(y1), int(y2))
            for j in range(min(int(y1), int(y2)), t + 1, 1):
                blocked.add((int(x1), j))
            if t > max_y:
                max_y = t
        else:
            for j in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1, 1):
                blocked.add((j, int(y1)))

blocked2 = deepcopy(blocked)

for i in range(1000):
    blocked2.add((i, max_y + 2))

s = (500, 0)
r = 0
dirs = [(0, 1), (-1, 1), (1, 1)]
done = False

while not done:
    for d in dirs:
        if (s[0] + d[0], s[1] + d[1]) not in blocked:
            s = (s[0] + d[0], s[1] + d[1])
            if s[1] == max_y:
                done = True
            break
    else:
        blocked.add(s)
        r += 1
        s = (500, 0)

print(r)

r = 0
s = (500, 0)
while True:
    if (500, 0) in blocked2:
        break
    for d in dirs:
        if (s[0] + d[0], s[1] + d[1]) not in blocked2:
            s = (s[0] + d[0], s[1] + d[1])
            break
    else:
        blocked2.add(s)
        r += 1
        s = (500, 0)

print(r)
