from operator import itemgetter
from collections import deque

lines = open('in.txt').read().split('\n')


def get_neighbors(c):
    return [(c[0] - d[0], c[1] - d[1], c[2] - d[2]) for d in
            [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


def is_inside(missing_cube):
    q = deque([missing_cube])
    visited = set()

    while len(q) > 0:
        c = q.popleft()

        if c[0] > max_x or c[1] > max_y or c[2] > max_z:
            return False

        for n in get_neighbors(c):
            if n not in visited and n not in cubes:
                visited.add(n)
                q.append(n)

    return True


cubes = set()
sides = 0
for line in lines:
    x, y, z = [int(x) for x in line.split(",")]
    cubes.add((x, y, z))

for cube in cubes:
    sides += len([x for x in get_neighbors(cube) if x not in cubes])

print(sides)

max_x = max(cubes, key=itemgetter(0))[0] + 1
max_y = max(cubes, key=itemgetter(1))[1] + 1
max_z = max(cubes, key=itemgetter(2))[2] + 1

all_cubes = set()
missing = [(x, y, z) for x in range(1, max_x) for y in range(1, max_y) for z in range(1, max_z)
           if (x, y, z) not in cubes]

trapped_cubes = set()
for m in missing:
    if is_inside(m):
        trapped_cubes.add(m)

area = 0
for cube in cubes:
    for neighbor in get_neighbors(cube):
        if neighbor not in cubes and neighbor not in trapped_cubes:
            area += 1

print(area)
