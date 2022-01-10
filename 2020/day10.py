from math import prod

with open('input') as file:
    adapters = list(map(int, file.readlines()))

# Sort the list
adapters.sort()

# Part 01
jolts = [0] + adapters + [adapters[-1] + 3]
diffs = [jolts[i + 1] - jolts[i] for i in range(len(jolts) - 1)]
print(diffs.count(1) * diffs.count(3))

# Part 02
count = 0
continous = []
# Find number of continous 1 betweens 3
for diff in diffs:
    if diff == 1:
        count += 1
    else:
        if count > 0:
            continous.append(count)
            count = 0

# Print product of combinations possible
# Combinations possible for:
#   3 1 1 3         is 2
#   3 1 1 1 3       is 4
#   3 1 1 1 1 3     is 7
#   3 1 1 1 1 1 3   is 11
#   Formula: sum of all value until (n-1) plus 1 --> (n-1)*n/2 + 1
print(prod([int(((value - 1) * value) / 2 + 1) for value in continous]))