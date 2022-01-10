def get_input():
    height_map = []
    with open("input") as file:
        lines = file.readlines()
        for line in lines:
            height_map.append(list(map(int, list(line.strip()))))
    return height_map


def part01(height_map):
    neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    low_points = []
    low_points_pos = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            for x, y in neighbours:
                if 0 <= i + x < len(height_map) and 0 <= j + y < len(height_map[0]):
                    neighbour = height_map[i + x][j + y]
                    if height_map[i][j] >= neighbour:
                        break
            else:
                low_points.append(height_map[i][j])
                low_points_pos.append((i, j))
    print(sum(low_points) + len(low_points))
    return low_points_pos


def create_basin(basin, seen, height_map):
    neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    i, j = seen[-1]
    for x, y in neighbours:
        if 0 <= i + x < len(height_map) and 0 <= j + y < len(height_map[0]):
            pos_x, pos_y = i + x, j + y
            neighbour = height_map[pos_x][pos_y]
            if (pos_x, pos_y) not in seen and neighbour != 9:
                basin.append(height_map[pos_x][pos_y])
                seen.append((pos_x, pos_y))
                create_basin(basin, seen, height_map)


def part02(height_map, low_points_pos):
    basins = []
    for x, y in low_points_pos:
        basin = [height_map[x][y]]
        create_basin(basin, [(x, y)], height_map)
        basins.append(basin)
    basins = sorted(basins, key=lambda x: len(x), reverse=True)
    result = 1
    for i in range(3):
        result *= len(basins[i])
    print(result)


if __name__ == "__main__":
    height_map = get_input()
    low_points_pos = part01(height_map)
    part02(height_map, low_points_pos)
