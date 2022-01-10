import os


def packet_scanner_1(puzzle_input):
    # Depth: range
    layout = {}
    for line in puzzle_input:
        # x: y -> [x, y]
        values = list(map(int, line.split(': ')))
        # {x: y}
        layout[values[0]] = values[1]

    firewall = {}
    # Generate initial state of firewall
    for depth in layout:
        firewall[depth] = 0

    trip_severity = 0
    end = max(list(layout)) + 1
    for depth in range(end):
        if depth in list(firewall):
            if firewall[depth] == 0:
                trip_severity += depth * layout[depth]
        # Move
        next_picosecond(layout, firewall)

    print(trip_severity)


def packet_scanner_2(puzzle_input):
    # Depth: range
    layout = {}
    for line in puzzle_input:
        # x: y -> [x, y]
        values = list(map(int, line.split(': ')))
        # {x: y}
        layout[values[0]] = values[1]

    freeze_state = {}
    # Generate initial state of firewall
    for depth in layout:
        freeze_state[depth] = 0

    delay = 0

    while 1:
        firewall = freeze_state.copy()
        end = max(list(layout)) + 1
        for depth in range(end):
            if depth in list(firewall):
                if firewall[depth] == 0:
                    break
            # Move
            next_picosecond(layout, firewall)
        else:
            break

        delay += 1

        next_picosecond(layout, freeze_state)

    print(delay)


def next_picosecond(layout, firewall):
    for depth in firewall:
        if firewall[depth] == layout[depth] - 1:
            firewall[depth] = -(firewall[depth])
        firewall[depth] += 1


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '/' + 'day13.txt') as file:
        puzzle_input = file.readlines()
    return puzzle_input


def main():
    puzzle_input = get_puzzle_input()
    packet_scanner_1(puzzle_input)
    packet_scanner_2(puzzle_input)


if __name__ == '__main__':
    main()