import re
import time

lines = open('in.txt').read().split('\n')

s = set()

start = time.time()
data = []

distance = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])

for line in lines:
    x1, y1, x2, y2 = [int(x) for x in re.findall(r'-?\d+\.?\d*', line)]
    r = abs(x1 - x2) + abs(y1 - y2)
    d = abs(y1 - 2000000)
    data.append([x1, y1, r])
    s.update(range(x1 - (r - d), x1 + (r - d)))

print(len(s))
print(f'Part 1: {time.time() - start}')

start = time.time()
# Initial solution is in 15_p2_brute_force.py
# + 1 intersection trick
pos_coef, neg_coef = [], []
for d in data:
    x, y, r = d
    pos_coef.extend([y - x + r + 1, y - x - r - 1])
    neg_coef.extend([x + y + r + 1, x + y - r - 1])

# keep only duplicates
pos_coef = set([x for x in pos_coef if pos_coef.count(x) >= 2])
neg_coef = set([x for x in neg_coef if neg_coef.count(x) >= 2])

for x, y in zip(pos_coef, neg_coef):
    intersection = ((y - x) // 2, (x + y) // 2)

    if 0 < intersection[0] < 4000000 and 0 < intersection[1] < 4000000 and \
            all(distance(intersection, (r[0], r[1])) > r[2] for r in data):
        print(intersection[0] * 4000000 + intersection[1])

print(f'Part 2: {time.time() - start}')
