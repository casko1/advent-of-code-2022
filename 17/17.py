orders = list(open('in.txt').read())
test = {}

rocks = [
    [[2, 4], [3, 4], [4, 4], [5, 4]],
    [[3, 6], [2, 5], [3, 5], [4, 5], [3, 4]],
    [[2, 4], [3, 4], [4, 4], [4, 5], [4, 6]],
    [[2, 4], [2, 5], [2, 6], [2, 7]],
    [[2, 4], [3, 4], [2,  5], [3, 5]]
]

directions = {'<': (-1, -1), '>': (1, 7)}

highest_y = 0
blocked = set([(x, 0) for x in range(7)])

# rock index, direction index
states = {}
dir_index = 0

stop = False
for i in range(1000000000000):
    rock = [[c[0], c[1] + highest_y] for c in rocks[i % 5]]

    if stop:
        break

    if i == 2022:
        print(highest_y)

    while True:
        dir_index %= len(orders)
        key = (i % 5, dir_index)
        dir_index += 1
        order = orders.pop(0)
        d = directions[order]

        if key in states:
            previous_index, prev_highest_y = states[key]
            diff = i - previous_index

            if i % diff == 1000000000000 % diff:
                cycle_length = highest_y - prev_highest_y
                remaining = 1000000000000 - i
                print(prev_highest_y + (cycle_length * ((remaining // diff) + 1)))
                stop = True
                break

        states[key] = (i, highest_y)

        if not any((c[0] + d[0], c[1]) in blocked for c in rock) and not any(x for x in rock if x[0] + d[0] == d[1]):
            for c in rock:
                c[0] += d[0]

        if any((c[0], c[1] - 1) in blocked for c in rock):
            prev_highest = highest_y
            for c in rock:
                blocked.add((c[0], c[1]))
                if c[1] > highest_y:
                    highest_y = c[1]

            orders.append(order)
            break

        for c in rock:
            c[1] -= 1

        orders.append(order)
