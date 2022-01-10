def get_input():
    # Get information
    with open('input') as file:
        data = file.read().split(',')
    opcodes = list(map(int, data))
    return opcodes


def part01():
    opcodes = get_input()
    # Initial step - replacement
    opcodes[1] = 12
    opcodes[2] = 2
    for i in range(0, len(opcodes), 4):
        (i1, i2, i3) = opcodes[i + 1:i + 4]
        if opcodes[i] == 99:
            break
        elif opcodes[i] == 1:
            opcodes[i3] = opcodes[i1] + opcodes[i2]
        elif opcodes[i] == 2:
            opcodes[i3] = opcodes[i1] * opcodes[i2]
    print(opcodes[0])


def part02():
    opcodes = get_input()
    for x in range(100):
        for y in range(100):
            memory = opcodes[:]
            memory[1] = x
            memory[2] = y
            for i in range(0, len(memory), 4):
                (i1, i2, i3) = memory[i + 1:i + 4]
                if memory[i] == 99:
                    break
                elif memory[i] == 1:
                    memory[i3] = memory[i1] + memory[i2]
                elif opcodes[i] == 2:
                    memory[i3] = memory[i1] * memory[i2]
            if memory[0] == 19690720:
                print(memory[1:3])
                return


if __name__ == '__main__':
    part01()
    part02()