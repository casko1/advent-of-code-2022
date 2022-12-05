import re
from copy import deepcopy

lines = open('in.txt').read().split('\n\n')

crates = lines[0].split('\n')
num_arr = int(crates[-1][len(crates[-1]) - 1])
crates_a = [[] for _ in range(num_arr)]
orders = [list(map(int, re.findall(r'\d+', line))) for line in lines[1].split('\n')]

for line in crates:
    for i in range(0, len(line), 4):
        crate = line[i: i+3]
        if len(crate.strip()) > 1:
            crates_a[i//4].append(crate[1])

crates_a_2 = deepcopy(crates_a)

for order in orders:
    a, f, t = order
    for i in range(a):
        crates_a[t - 1].insert(0, crates_a[f - 1].pop(0))
        crates_a_2[t - 1].insert(0, crates_a_2[f - 1].pop(a - 1 - i))

print(''.join(s[0] for s in crates_a))
print(''.join(s[0] for s in crates_a_2))
