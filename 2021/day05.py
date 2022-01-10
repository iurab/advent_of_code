import numpy


def get_input():
    lines = []
    with open("input") as file:
        rlines = file.readlines()
        for rline in rlines:
            points = rline.strip().split(" -> ")
            lines.append(
                [
                    tuple(map(int, points[0].split(","))),
                    tuple(map(int, points[1].split(","))),
                ]
            )
    return lines


def part01(lines):
    # Find max X and Y
    all_x = [point[0][0] for point in lines] + [point[1][0] for point in lines]
    all_y = [point[0][1] for point in lines] + [point[1][1] for point in lines]
    hydro_map = numpy.zeros((max(all_x) + 1, max(all_y) + 1), int)
    for line in lines:
        (x1, y1), (x2, y2) = line
        # Mark on map
        # Vertical
        if x1 == x2:
            for j in range(min([y1, y2]), max([y1, y2]) + 1):
                hydro_map[j][x1] += 1
            continue
        # Horizontal
        if y1 == y2:
            for i in range(min([x1, x2]), max([x1, x2]) + 1):
                hydro_map[y1][i] += 1
            continue
    print(numpy.sum(hydro_map > 1))


def part02(lines):
    # Find max X and Y
    all_x = [point[0][0] for point in lines] + [point[1][0] for point in lines]
    all_y = [point[0][1] for point in lines] + [point[1][1] for point in lines]
    hydro_map = numpy.zeros((max(all_x) + 1, max(all_y) + 1), int)
    for line in lines:
        (x1, y1), (x2, y2) = line
        # Mark on map
        # Vertical
        if x1 == x2:
            for j in range(min([y1, y2]), max([y1, y2]) + 1):
                hydro_map[j][x1] += 1
            continue
        # Horizontal
        if y1 == y2:
            for i in range(min([x1, x2]), max([x1, x2]) + 1):
                hydro_map[y1][i] += 1
            continue
        # Diagonal
        while x1 != x2 and y1 != y2:
            hydro_map[y1][x1] += 1
            x1 += 1 if x1 < x2 else -1
            y1 += 1 if y1 < y2 else -1
        hydro_map[y1][x1] += 1
    print(numpy.sum(hydro_map > 1))


if __name__ == "__main__":
    lines = get_input()
    part01(lines)
    part02(lines)
