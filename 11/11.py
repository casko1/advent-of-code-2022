import math
import re
import operator

lines = open('in.txt').read().split('\n\n')
ops = {"+": operator.add, "*": operator.mul}


def get_lambda(op):
    return lambda x: ops[op[-2]](x, int(op[-1]) if op[-1].isnumeric() else x)


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.divisor = None
        self.true_m = None
        self.false_m = None
        self.inspected = 0


m = [Monkey() for _ in range(len(lines))]

for i in range(len(lines)):
    spl = lines[i].split('\n')
    m[i].items += list(map(int, re.findall(r'\d+', spl[1])))
    operator_spl = spl[2].split(' ')
    m[i].operation = get_lambda(operator_spl)
    m[i].divisor = int(re.findall(r'\d+', spl[3])[0])
    m[i].true_m = int(re.findall(r'\d+', spl[4])[0])
    m[i].false_m = int(re.findall(r'\d+', spl[5])[0])

lcm = math.lcm(*[x.divisor for x in m])


def monkey_business(n, divide):
    for i in range(n):
        for j in range(len(m)):
            while len(m[j].items) > 0:
                m[j].inspected += 1
                it = m[j].operation(m[j].items.pop()) % lcm
                if divide:
                    it //= 3
                if it % m[j].divisor == 0:
                    m[m[j].true_m].items.append(it)
                else:
                    m[m[j].false_m].items.append(it)

    a = sorted([x.inspected for x in m])
    return a[-1] * a[-2]


print(monkey_business(20, True))
print(monkey_business(10000, False))
