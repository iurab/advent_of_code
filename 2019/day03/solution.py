MOVE = {'U': [1, 0], 'D': [-1, 0], 'L': [0, -1], 'R': [0, 1]}


def get_input():
    # Get information
    paths = []
    with open('input', 'r') as file:
        lines = file.readlines()
    for line in lines:
        paths.append(line.split(','))
    return paths


def process_wire(path):
    current_pos = [0, 0]
    wire_path = []
    for point in path:
        direction = point[0]
        steps = int(point[1:])
        for _ in range(steps):
            current_pos[0] += MOVE[direction][0]
            current_pos[1] += MOVE[direction][1]
            wire_path.append(tuple(current_pos))
    return wire_path


def part01():
    paths = get_input()
    wire1 = process_wire(paths[0])
    wire2 = process_wire(paths[1])
    intersections = set(wire1) & set(wire2)
    print(min(abs(x) + abs(y) for x, y in intersections))


def part02():
    paths = get_input()
    wire1 = process_wire(paths[0])
    wire2 = process_wire(paths[1])
    intersections = set(wire1) & set(wire2)
    print(
        min(2 + wire1.index(inter) + wire2.index(inter)
            for inter in intersections))


if __name__ == '__main__':
    part01()
    part02()