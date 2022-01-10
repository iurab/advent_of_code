import copy


def get_input():
    binaries = []
    with open("input") as file:
        lines = file.readlines()
        for line in lines:
            # Add all characters of the line in the list
            binaries.append(list(line.strip()))
    return binaries


def get_column(binaries, j):
    column = []
    # Loop from Top -> Bottom
    for i in range(len(binaries)):
        column.append(binaries[i][j])
    return column


def most_common(binary):
    if binary.count("1") >= binary.count("0"):
        return "1"
    else:
        return "0"


def less_common(binary):
    if binary.count("1") >= binary.count("0"):
        return "0"
    else:
        return "1"


def part01(binaries):
    gamma = []
    epsilon = []
    # Loop from Left -> Right
    for j in range(len(binaries[0])):
        column = get_column(binaries, j)

        # Add bits to gamma and epsilon
        gamma.append(most_common(column))
        epsilon.append(less_common(column))

    # Transfrom list to string and convert it to number from base 2
    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)
    print(gamma * epsilon)


def part02(binaries):
    # Oxygen
    # Make a copy of the "matrix"
    bin_oxygen = copy.deepcopy(binaries)
    for j in range(len(bin_oxygen[0])):
        column = get_column(bin_oxygen, j)
        bit = most_common(column)
        bin_oxygen = list(filter(lambda x: (x[j] == bit), bin_oxygen))
        if len(bin_oxygen) == 1:
            break
    oxygen = int("".join(bin_oxygen[0]), 2)
    # CO2
    # Make a copy of the "matrix"
    bin_co2 = copy.deepcopy(binaries)
    for j in range(len(bin_co2[0])):
        column = get_column(bin_co2, j)
        bit = less_common(column)
        bin_co2 = list(filter(lambda x: (x[j] == bit), bin_co2))
        if len(bin_co2) == 1:
            break
    co2 = int("".join(bin_co2[0]), 2)
    print(oxygen * co2)


if __name__ == "__main__":
    binaries = get_input()
    part01(binaries)
    part02(binaries)
