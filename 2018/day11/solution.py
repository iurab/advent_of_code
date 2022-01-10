import numpy as np


def get_power(i, j):
    x = i + 1
    y = j + 1
    serial_number = 1309
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    return power_level // 100 % 10 - 5


def solution():
    grid = np.fromfunction(get_power, (300, 300))
    # Find 3x3 with the largest power
    for width in range(3, 300):
        windows = sum(grid[i:i - width + 1 or None, j:j - width + 1 or None]
                      for i in range(width) for j in range(width))
        maximum = int(windows.max())
        location = np.where(windows == maximum)
        print(width, maximum, location[0][0] + 1, location[1][0] + 1)
    # Find XxX (variable size) with the largest power
    # largest_power = 0
    # identifier = ()
    # for size in range(1, 301):
    #     for i in range(300 - size):
    #         for j in range(300 - size):
    #             value = np.sum(grid[i:i + size, j:j + size])
    #             if value > largest_power:
    #                 identifier = (i + 1, j + 1, size)
    #                 largest_power = value
    # print(identifier)


if __name__ == "__main__":
    solution()