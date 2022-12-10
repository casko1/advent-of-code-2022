lines = open('in.txt').read().split('\n')
path = ['/']
sizes = {}
del lines[0]
for line in lines:
    spl = line.split(' ')
    if spl[0] == '$':
        if spl[1] == 'cd':
            if spl[2] == '..':
                path.pop()
            else:
                path.append(path[-1] + '|' + spl[2])
    elif spl[0].isnumeric():
        for p in path:
            if p in sizes:
                sizes[p] += int(spl[0])
            else:
                sizes[p] = int(spl[0])

print(sum(s for s in sizes.values() if s <= 100000))
print(min(s for s in sizes.values() if s >= sizes['/'] - 40000000))
