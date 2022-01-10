from typing import DefaultDict
from parse import parse
from itertools import product

with open('input') as file:
    lines = file.readlines()

# Part 01
memory = DefaultDict(int)
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for line in lines:
    if 'mask' in line:
        # Extract mask
        mask = parse('mask = {}', line)[0]
    else:
        # Extract instruction
        r = parse('mem[{address:d}] = {value:d}', line)
        address = r['address']
        value = r['value']

        b_value = '0' * (36 - len(bin(value)[2:])) + bin(value)[2:]
        b_new_value = ''
        for i in range(len(mask)):
            if mask[i] == 'X':
                # Dont change
                b_new_value += b_value[i]
            else:
                # Use the bit defined in the mask
                b_new_value += mask[i]
            memory[address] = int(b_new_value, 2)
print(sum(memory.values()))

# Part 02
memory = DefaultDict(int)
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
for line in lines:
    if 'mask' in line:
        # Extract mask
        mask = parse('mask = {}', line)[0]
    else:
        # Extract instruction
        r = parse('mem[{address:d}] = {value:d}', line)
        address = r['address']
        value = r['value']
        b_address = '0' * (36 - len(bin(address)[2:])) + bin(address)[2:]

        for bits in product('01',repeat=mask.count('X')):
            i_b = 0            
            b_new_address = ''
            for i_a in range(len(mask)):
                if mask[i_a] == 'X':
                    # Use possible combination
                    b_new_address += bits[i_b]
                    i_b += 1
                elif mask[i_a] == '1':
                    # Replace with 1
                    b_new_address += '1'
                else:
                    # Don't change it
                    b_new_address += b_address[i_a]
            memory[int(b_new_address,2)] = value
print(sum(memory.values()))
