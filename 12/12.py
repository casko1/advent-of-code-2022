lines = open('in.txt').read().split('\n')

m = []
start = None
starting_positions = []
end = None
for i in range(len(lines)):
    tmp = []
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            start = (i, j)
            tmp.append(0)
        elif lines[i][j] == 'E':
            end = (i, j)
            tmp.append(25)
        elif lines[i][j] == 'a':
            starting_positions.append((i, j))
            tmp.append(0)
        else:
            tmp.append(ord(lines[i][j]) - ord('a'))

    m.append(tmp)


def find_shortest(distance_dict, queue):
    while len(queue) > 0:
        c = queue.pop(0)

        if c == end:
            return distance_dict[c]

        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_c = (c[0] + d[0], c[1] + d[1])
            if new_c[0] in range(len(m)) and new_c[1] in range(len(m[0])) \
                    and m[new_c[0]][new_c[1]] - 1 <= m[c[0]][c[1]] and new_c not in distance_dict:

                distance_dict[new_c] = distance_dict[c] + 1
                queue.append(new_c)


print(find_shortest({start: 0}, [start]))

starting_positions.append(start)
d = {}
q = []
for s in starting_positions:
    d[s] = 0
    q.append(s)

print(find_shortest(d, q))
