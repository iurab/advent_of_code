def generate_matrix_1(size):
    
    directions = {0: [0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}
    x, y = int((size - 1) / 2), int((size - 1) / 2)
    next_mov = 0
    steps_to_make = 1
    # Generate matrix
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    # Set initial value
    value = 1
    matrix[x][y] = value

    while 1:
        for _ in range(2):
            for _ in range(steps_to_make):
                x += directions[next_mov][0]
                y += directions[next_mov][1]
                value += 1
                if value > size ** 2:
                    return matrix
                matrix[x][y] = value
            if next_mov + 1 > 3:
                next_mov = 0
            else:
                next_mov += 1
        steps_to_make += 1

    return matrix


def find_position(matrix, value):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == value:
                return [i,j]


def first_value_written(size, max_value):
    
    directions = {0: [0, 1], 1: [-1, 0], 2: [0, -1], 3: [1, 0]}
    x, y = int((size - 1) / 2), int((size - 1) / 2)
    next_mov = 0
    steps_to_make = 1
    # Generate matrix
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    # Set initial value
    value = 1z
    matrix[x][y] = value

    while 1:
        for _ in range(2):
            for _ in range(steps_to_make):
                x += directions[next_mov][0]
                y += directions[next_mov][1]
                # Calculate value
                value = matrix[x][y] + matrix[x - 1][y] + matrix[x - 1][y + 1] + matrix[x - 1][y - 1] + matrix[x][y + 1] + matrix[x + 1][y + 1] + matrix[x][y - 1] + matrix[x + 1][y - 1] + matrix[x + 1][y]
                if value > max_value:
                    return value
                matrix[x][y] = value
            if next_mov + 1 > 3:
                next_mov = 0
            else:
                next_mov += 1
        steps_to_make += 1

    return matrix

matrix = generate_matrix_1(571)
position = find_position(matrix, 325489)
print('Distance: ', abs(position[0] - 286) + abs(position[1] - 286))
next_value = first_value_written(571, 325489)
print('Next value', next_value)