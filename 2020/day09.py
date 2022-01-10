from itertools import combinations

with open('input') as file:
    data = file.readlines()
    data = list(map(int, data))

def gen_XMAS(preamble):
    return [x + y for x, y in combinations(preamble, 2)]

# Part 01
for i in range(25,len(data)):
    # Find weakness
    if data[i] not in gen_XMAS(data[i-25:i]):
        print(weakness:=data[i])
        break

# Part 02
cont_range = []
for i in range(len(data) - 1):
    j = 2
    while (total:=sum(data[i:i+j])) < weakness:
        j += 1
    if total == weakness:
        cont_range = data[i:i+j]
        break

print(sum([min(cont_range),max(cont_range)]))