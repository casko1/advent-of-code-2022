from collections import defaultdict
import re
from itertools import product, combinations

lines = open('in.txt').read().split('\n')

nodes = set()
flow_rate = {}
distances = defaultdict(lambda: 99999)

for line in lines:
    n, fr, *neighbors = re.findall(r'[A-Z]{2}|[0-9]+', line[1:])
    nodes.add(n)
    for neighbor in neighbors:
        distances[n, neighbor] = 1

    if fr != '0':
        flow_rate[n] = int(fr)

# note to myself: don't use triple nested collection-based for loops
for a, b, c in product(nodes, repeat=3):
    distances[b, c] = min(distances[b, c], distances[b, a] + distances[a, c])


def find_optimal(current_node, unvisited_nodes, minutes):
    pressures = []

    for node in unvisited_nodes:
        if distances[current_node, node] < minutes:
            remaining_time = minutes - distances[current_node, node] - 1
            path_pressure = find_optimal(node, [x for x in unvisited_nodes if x != node], remaining_time)
            pressure = flow_rate[node] * (minutes - distances[current_node, node] - 1) + path_pressure
            pressures.append(pressure)

    return 0 if len(pressures) == 0 or len(unvisited_nodes) == 0 else max(pressures)


print(find_optimal('AA', flow_rate, 30))
fr = flow_rate.keys()
combs = [[x, tuple(y for y in fr if y not in x)] for x in combinations(fr, len(fr)//2)]
print(max([find_optimal('AA', p1, 26) + find_optimal('AA', p2, 26) for p1, p2 in combs]))
