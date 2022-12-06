line = open('in.txt').read().split('\n')[0]


def find(n):
    for i in range(len(line)):
        if len(set(line[i:i+n])) == n:
            print(i + n)
            return


find(4)
find(14)