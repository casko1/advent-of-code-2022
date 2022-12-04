outcomes = {'A': {'Z': 3, 'X': 4, 'Y': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'Y': 2, 'Z': 6, 'X': 7}}
index = {'X': 0, 'Y': 1, 'Z': 2}
lines = [x for x in open('in.txt').read().split('\n') if len(x) > 0]
print(sum(outcomes[x[0]][x[2]] for x in lines))
print(sum(list(outcomes[x[0]].values())[index[x[2]]] for x in lines))
