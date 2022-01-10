def get_input():
    with open('input') as file:
        data = file.read().split(',')
    opcodes = list(map(int, data))
    return opcodes


def part01():
    opcodes = get_input()
    # Replace
    opcodes[opcodes[1]] = 1
    pos = 2
    while opcodes[pos] != 99:
        # Get command
        command = opcodes[pos] % 100
        # Get mode of parameters
        nr_param = 1 if command in [3, 4] else 3
        modes = []
        for i in range(2, 2 + nr_param):
            modes.append(opcodes[pos] // 10**i % 10)
        # Get parameters position in opcode
        parameters = []
        for i in range(len(modes)):
            if modes[i] == 0:
                # Position mode
                parameters.append(opcodes[pos + 1 + i])
            else:
                # Immediate mode
                parameters.append(pos + 1 + i)
        # Execute command
        if command == 4:
            # Print
            print(opcodes[parameters[0]])
        elif command == 1:
            # Sum
            opcodes[parameters[2]] = opcodes[parameters[0]] + opcodes[
                parameters[1]]
        elif command == 2:
            # Sum
            opcodes[parameters[2]] = opcodes[parameters[0]] * opcodes[
                parameters[1]]
        pos += 1 + nr_param


def part02():
    opcodes = get_input()
    # Replace
    opcodes[opcodes[1]] = 5
    pos = 2
    while opcodes[pos] != 99:
        # Get command
        command = opcodes[pos] % 100
        # Get mode of parameters
        if command in [3, 4]:
            nr_param = 1
        elif command in [5, 6]:
            nr_param = 2
        elif command in [1, 2, 7, 8]:
            nr_param = 3
        modes = []
        for i in range(2, 2 + nr_param):
            modes.append(opcodes[pos] // 10**i % 10)
        # Get parameters position in opcode
        parameters = []
        for i in range(len(modes)):
            if modes[i] == 0:
                # Position mode
                parameters.append(opcodes[pos + 1 + i])
            else:
                # Immediate mode
                parameters.append(pos + 1 + i)
        # Execute command
        if command == 1:
            # Sum
            opcodes[parameters[2]] = opcodes[parameters[0]] + opcodes[
                parameters[1]]
            pos += 1 + nr_param
        elif command == 2:
            # Multiply
            opcodes[parameters[2]] = opcodes[parameters[0]] * opcodes[
                parameters[1]]
            pos += 1 + nr_param
        elif command == 4:
            # Print
            print(opcodes[parameters[0]])
            pos += 1 + nr_param
        elif command == 5:
            # Jump if TRUE
            if opcodes[parameters[0]] != 0:
                pos = opcodes[parameters[1]]
            else:
                pos += 1 + nr_param
        elif command == 6:
            # Jump if FALSE
            if opcodes[parameters[0]] == 0:
                pos = opcodes[parameters[1]]
            else:
                pos += 1 + nr_param
        elif command == 7:
            # Less than
            opcodes[parameters[2]] = 1 if opcodes[parameters[0]] < opcodes[
                parameters[1]] else 0
            pos += 1 + nr_param
        elif command == 8:
            # Equals
            opcodes[parameters[2]] = 1 if opcodes[parameters[0]] == opcodes[
                parameters[1]] else 0
            pos += 1 + nr_param


if __name__ == '__main__':
    # part01()
    part02()