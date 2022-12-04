lines = open('in.txt').read().split('\n')

fully_contained = 0
overlap = 0

for line in lines:
    pairs = line.split(',')
    start1, end1 = list(map(int, pairs[0].split('-')))
    start2, end2 = list(map(int, pairs[1].split('-')))

    if start1 <= start2 and end2 <= end1 or start2 <= start1 and end1 <= end2:
        fully_contained += 1

    if not (end1 < start2 or end2 < start1):
        overlap += 1

print(fully_contained)
print(overlap)

