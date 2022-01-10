import numpy as np


def get_input():
    with open('input') as file:
        puzzle_input = file.read().splitlines()
    # Processes input
    coordinates = []
    for line in puzzle_input:
        values = line.split(', ')
        coordinates.append((int(values[0]), int(values[1])))
    return coordinates


def distance(point_a, point_b):
    x_a, y_a = point_a
    x_b, y_b = point_b
    return abs(x_a - x_b) + abs(y_a - y_b)


def part01(coordinates):
    # Find X maximum coordinate
    x_max = max([x for (x, _) in coordinates])
    # Find Y maximum coordinate
    y_max = max([y for (_, y) in coordinates])
    # print(x_max, y_max)
    # Create matrix
    matrix = np.zeros((x_max + 1, y_max + 1), dtype=np.int)
    # Mark initial positions
    marker = 1
    for (x, y) in coordinates:
        matrix[x, y] = marker
        marker += 1
    # For each point find the nearest point
    for i in range(x_max):
        for j in range(y_max):
            if matrix[i, j] != 0:
                continue
            distances = [distance((i, j), marker) for marker in coordinates]
            min_distance = min(distances)
            # Modify value only if we have one minimum
            if len(np.where(distances == min_distance)) == 1:
                matrix[i, j] = distances.index(min_distance) + 1
    # Remove areas that can be infinite
    for i in range(x_max):
        # Left
        remove = matrix[i][0]
        matrix[matrix == remove] = 0
        # Right
        remove = matrix[i][y_max - 1]
        matrix[matrix == remove] = 0
    for j in range(y_max):
        # Up
        remove = matrix[0][j]
        matrix[matrix == remove] = 0
        # Down
        remove = matrix[x_max - 1][j]
        matrix[matrix == remove] = 0

    # Find the area for each marker
    areas = []
    for index, _ in enumerate(coordinates):
        marker = index + 1
        areas.append(len(np.where(matrix == marker)[0]))
    print(max(areas))


def part02(coordinates):
    # Find X maximum coordinate
    x_max = max([x for (x, _) in coordinates])
    # Find Y maximum coordinate
    y_max = max([y for (_, y) in coordinates])
    # print(x_max, y_max)
    # Create matrix
    matrix = np.zeros((x_max + 1, y_max + 1), dtype=np.int)
    # For each point find the distances
    for i in range(x_max):
        for j in range(y_max):
            distances = [distance((i, j), marker) for marker in coordinates]
            # Mark point if coordinates are safe
            if sum(distances) < 10000:
                matrix[i, j] = 1
    print(np.sum(matrix))


if __name__ == '__main__':
    coordinates = get_input()
    # print(coordinates)
    part01(coordinates)
    part02(coordinates)