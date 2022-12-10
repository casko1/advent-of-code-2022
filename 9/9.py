lines = open('in.txt').read().split('\n')
nodes = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited = [set() for x in range(10)]
neighbor_directions = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
directions = {'R': [1, 0], 'L': [-1, 0], 'D': [0, -1], 'U': [0, 1]}


def adjust(parent, child):
    x_diff = parent[0] - child[0]
    y_diff = parent[1] - child[1]
    if [x_diff, y_diff] in neighbor_directions:
        return 0, 0

    m = [100, 100]
    move = None

    for d in neighbor_directions:
        x_adj = child[0] + d[0]
        y_adj = child[1] + d[1]
        if (abs(parent[0] - x_adj) + abs(parent[1] - y_adj)) < m[0] + m[1]:
            move = d
            m = [abs(parent[0] - x_adj), abs(parent[1] - y_adj)]

    return move


for line in lines:
    spl = line.split(' ')
    for i in range(int(spl[1])):
        nodes[0][0] += directions[spl[0]][0]
        nodes[0][1] += directions[spl[0]][1]
        for j in range(1, len(nodes)):
            adjustment = adjust(nodes[j-1], nodes[j])
            nodes[j][0] += adjustment[0]
            nodes[j][1] += adjustment[1]
            visited[j].add((nodes[j][0], nodes[j][1]))

print(len(visited[1]), len(visited[9]))
