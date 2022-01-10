import string
from collections import defaultdict

# def duet_1(puzzle_input):
#     instructions = puzzle_input
#     reg = defaultdict(int)
#     for char in string.ascii_letters:
#         reg[char] = 0
#     position = 0
#     last_played = None
#     while True:
#         instr = instructions[position]
#         if 'set' in instr:
#             i_set(instr, reg)
#         elif 'add' in instr:
#             i_add(instr, reg)
#         elif 'mul' in instr:
#             i_mul(instr, reg)
#         elif 'mod' in instr:
#             i_mod(instr, reg)
#         elif 'jgz' in instr:
#             position += i_jgz(instr, reg) - 1
#         elif 'snd' in instr:
#             last_played = i_snd(instr, reg)
#         elif 'rcv' in instr:
#             if i_rcv(instr, reg):
#                 print(last_played)
#                 break
#         position += 1
#         if position == len(instructions):
#             break


def duet_2(puzzle_input):
    instructions = puzzle_input
    reg1 = defaultdict(int)
    reg2 = reg1.copy()
    # Set program ID
    reg2['p'] = 1
    regs = [reg1, reg2]
    pos = [0, 0]
    prg = 0
    i = pos[prg]
    # Create buffer for each program
    buff = [[], []]
    status = ['ok', 'ok']
    # Counter
    count1 = 0
    while True:
        # Select register
        regx = regs[prg]
        instr = instructions[i]
        if 'set' in instr:
            i_set(instr, regx)
        elif 'add' in instr:
            i_add(instr, regx)
        elif 'mul' in instr:
            i_mul(instr, regx)
        elif 'mod' in instr:
            i_mod(instr, regx)
        elif 'jgz' in instr:
            i += i_jgz(instr, regx) - 1
        elif 'snd' in instr:
            buff[1 - prg].append(i_snd(instr, regx))
            if prg == 1:
                count1 += 1
            if status[1 - prg] == 'wait':
                status[1 - prg] = 'ok'
        elif 'rcv' in instr:
            if len(buff[prg]) != 0:
                i_rcv(instr, regx, buff[prg].pop(0))
            else:
                # Nothing to receive
                status[prg] = 'wait'
                if status[1 - prg] != 'ok':
                    break
                else:
                    pos[prg] = i
                    prg = 1 - prg
                    i = pos[prg] - 1
        i += 1

        if not 0 <= i < len(instructions):
            status[prg] = 'done'
            if status[1 - prg] != 'ok':
                break
            else:
                pos[prg] = i
                prg = 1 - prg
                i = pos[prg]

    print(count1)


def get(element, register):
    try:
        return int(element)
    except ValueError:
        return register[element]


def i_set(instruction, register):
    elements = instruction.strip().split(' ')
    # Set register value
    register[elements[1]] = get(elements[2], register)


def i_add(instruction, register):
    elements = instruction.strip().split(' ')
    # Set register value
    register[elements[1]] += get(elements[2], register)


def i_mul(instruction, register):
    elements = instruction.strip().split(' ')
    # Set register value
    register[elements[1]] *= get(elements[2], register)


def i_mod(instruction, register):
    elements = instruction.strip().split(' ')
    # Set register value
    register[elements[1]] %= get(elements[2], register)


def i_jgz(instruction, register):
    elements = instruction.strip().split(' ')
    if get(elements[1], register) != 0:
        return get(elements[2], register)
    else:
        return 1


def i_snd(instruction, register):
    elements = instruction.strip().split(' ')
    return get(elements[1], register)


def i_rcv(instruction, register, value):
    elements = instruction.strip().split(' ')
    register[elements[1]] = value


def get_puzzle_input():
    with open('day18.txt.') as file:
        puzzle_input = file.readlines()
    return puzzle_input


def main():
    puzzle_input = get_puzzle_input()
    duet_2(puzzle_input)


if __name__ == '__main__':
    main()
