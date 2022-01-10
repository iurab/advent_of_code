from collections import defaultdict


with open('input') as file:
    data = list(map(int, file.readline().split(',')))

# Part 01
position = defaultdict(lambda:-1)
for i in range(len(data) - 1):
    position[data[i]] = i

for i in range(len(data) - 1,30000000):
    if position[data[i]] == -1:
        position[data[i]] = i
        data.append(0)
    else:
        data.append(i - position[data[i]])
        position[data[i]] = i
print(data[30000000-1])