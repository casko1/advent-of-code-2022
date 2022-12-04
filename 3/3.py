import string

lines = open('in.txt').read().split('\n')
dup = [list(set(line[len(line) // 2:]) & set(line[:len(line) // 2])).pop() for line in lines]
print(sum(string.ascii_letters.index(c) for c in dup))
dup = [list(set.intersection(*map(set, lines[i:i + 3]))).pop() for i in range(0, len(lines), 3)]
print(sum(string.ascii_letters.index(c) for c in dup))
