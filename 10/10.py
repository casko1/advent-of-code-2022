lines = open('in.tx').read().split('\n')

marks = [20, 60, 100, 140, 180, 220]
x = 1
total = 0
strings = ["" for _ in range(6)]
sprite_pos = [0, 1, 2]
execute = []

for i in range(240):
    instruction = ""
    if len(execute) == 0:
        instruction = lines.pop(0).split()

    if i % 40 in sprite_pos:
        strings[i//40] += "#"
    else:
        strings[i//40] += "."

    if (i + 1) in marks:
        total += (i + 1) * x

    if len(execute) != 0:
        a = execute.pop(0)
        x += a
        sprite_pos = [p + int(a) for p in sprite_pos]

    if len(instruction) > 1 and len(execute) == 0:
        execute.append(int(instruction[1]))

print(total)
print('\n'.join(strings))
