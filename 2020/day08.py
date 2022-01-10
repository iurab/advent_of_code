import copy

with open('input') as file:
    lines = file.readlines()

code = []
for line in lines:
    code.append([line[0:3], int(line.strip()[4:])])

def compute(code):
    variable = index = 0
    checked = [0] * len(code)
    while index < len(code):
        if checked[index]:
            break
        instr, value = code[index]
        checked[index] = 1
        if instr == 'acc':
            variable += value
        if instr == 'jmp':
            index += value
            continue
        index += 1
    else:
        return True, variable
    return False, variable
    
# Part 01
print(compute(code)[1])


#Part 02
for index in range(len(code)):
    new_code = copy.deepcopy(code)
    if code[index][0] == 'nop':
        new_code[index][0] = 'jmp'
    elif code[index][0] == 'jmp':
        new_code[index][0] = 'nop'
    exit_status, variable = compute(new_code)
    if exit_status:
        print(variable)
        break
