lines = open('in.txt').read().split('\n\n')
sorted_elves = sorted(sum(map(int, line.strip().split('\n'))) for line in lines)
print(sorted_elves[-1])
print(sum(sorted_elves[-3:]))

