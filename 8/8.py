lines = open('in.txt').read().split('\n')

m = []
for line in lines:
    m.append(list(line))

out1 = 2 * len(m) + 2 * (len(m) - 2)


def p1(v, i, j, di, dj):
    if m[i + di][j + dj] >= v:
        return False

    if i + di == 0 or i + di == len(m) - 1 or j + dj == 0 or j + dj == len(m) - 1:
        return True

    return p1(v, i + di, j + dj, di, dj)


for i in range(1, len(m) - 1):
    for j in range(1, len(m) - 1):
        visibility = [p1(m[i][j], i, j, d[0], d[1]) for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]]
        if any(visibility):
            out1 += 1

print(out1)


def p2(v, i, j, di, dj):
    if i + di == 0 or i + di == len(m) - 1 or j + dj == 0 or j + dj == len(m) - 1 or m[i + di][j + dj] >= v:
        return 1

    return 1 + p2(v, i + di, j + dj, di, dj)


out2 = []

for i in range(1, len(m) - 1):
    for j in range(1, len(m) - 1):
        nums = [p2(m[i][j], i, j, d[0], d[1]) for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]]
        out2.append(nums[0] * nums[1] * nums[2] * nums[3])

print(max(out2))
