def get_input():
    # Get data
    commands = []
    with open("input") as file:
        lines = file.readlines()
        for line in lines:
            command, unit = line.strip().split()
            commands.append((command, int(unit)))
    return commands

def part01(commands):
    depth, horizontal = 0, 0
    for command, unit in commands:
        if command == "forward":
            horizontal += unit
        elif command == "up":
            depth -= unit
        else:
            depth += unit
    print(horizontal * depth)

def part02(commands):
    aim, depth, horizontal = 0, 0, 0
    for command, unit in commands:
        if command == "down":
            aim += unit
        elif command == "up":
            aim -= unit
        else:
            horizontal += unit
            depth += aim * unit
    print(horizontal * depth)

if __name__ == "__main__":
    commands = get_input()
    part01(commands)
    part02(commands)
