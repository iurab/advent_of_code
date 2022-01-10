from math import prod

with open('input') as file:
    lines = file.readlines()

early_t = int(lines[0].strip())
buses = list(map(int,[entry for entry in lines[1].strip().split(',') if entry.isdigit()]))

# Part 01
waiting_times = []
for bus in buses:
    waiting_times.append(bus - (early_t % bus))

print(min(waiting_times) * buses[waiting_times.index(min(waiting_times))])

# Part 02 -- apply Chinese Remainder Theorem
# https://www.youtube.com/watch?v=zIFehsBHB8o
buses = list(map(int,[entry if entry.isdigit() else -1 for entry in lines[1].strip().split(',')]))
# Generate list of MODs and REMAINDERs 
l_b = []
l_n = []
for index, bus in enumerate(buses):
    if bus == -1:
        continue
    l_n.append(bus)
    remainder = (bus - index % bus) if index % bus != 0 else 0
    l_b.append(remainder)

N = prod(l_n)
l_bNx = []
for i in range(len(l_b)):
    # Calculate Ni
    Ni = int(N / l_n[i])
    # Calculate xi - inverse of Ni
    xi = 1
    while True:
        if ((Ni % l_n[i]) * xi) % l_n[i] == 1:
            break
        xi += 1
    l_bNx.append(l_b[i] * Ni * xi)
print(sum(l_bNx) % N)
    


