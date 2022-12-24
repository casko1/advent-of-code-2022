from copy import deepcopy

lines = open('in.txt').read().split('\n')

nums = []

zero = None

for i in range(len(lines)):
    if lines[i] == '0':
        zero = (0, i)
    nums.append((int(lines[i]) * 811589153, i))


order = deepcopy(nums)

for _ in range(10):
    for n in order:
        current_index = nums.index(n)
        del nums[current_index]
        new_index = (current_index + n[0]) % len(nums)
        if new_index < 0:
            new_index += len(nums)
        nums.insert(new_index, n)

z_ind = nums.index(zero)
print(sum(nums[(x * 1000 % len(nums) + z_ind) % len(nums)][0] for x in [1, 2, 3]))
