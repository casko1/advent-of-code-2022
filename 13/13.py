packets = [eval(p.strip()) for pair in open('in.txt').read().split('\n\n') for p in pair.split('\n')]


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return None
        return l < r

    if isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])

    if isinstance(l, int) and isinstance(r, list):
        return compare([l], r)

    if isinstance(l, list) and isinstance(r, list):
        for j in range(min(len(l), len(r))):
            c = compare(l[j], r[j])
            if c is not None:
                return c
        return len(l) < len(r) if len(l) != len(r) else None


sum1 = 0
for i in range(0, len(packets), 2):
    p1 = packets[i]
    p2 = packets[i + 1]

    if compare(p1, p2):
        sum1 += (i + 2) // 2

print(sum1)

delims = [[[2]], [[6]]]
idx = []

for d in delims:
    s = 0
    for p in packets:
        if compare(p, d):
            s += 1
    idx.append(s)

print((idx[0] + 1) * (idx[1] + 2))
