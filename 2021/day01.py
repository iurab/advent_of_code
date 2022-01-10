def get_input():
    # Get data
    with open("input") as file:
        data = file.read().splitlines()
    # Adapt / convert information
    depths = list(map(int, data))
    return depths


def count_increase(values):
    count = 0
    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            count += 1
    return count


def part01(depths):
    count = count_increase(depths)
    print(count)


def part02(depths):
    # Generate windows
    windows = []
    for i in range(len(depths) - 2):
        window = depths[i] + depths[i + 1] + depths[i + 2]
        windows.append(window)
    count = count_increase(windows)
    print(count)


if __name__ == "__main__":
    depths = get_input()
    part01(depths)
    part02(depths)
