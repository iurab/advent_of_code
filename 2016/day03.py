import os

def triangles_1(puzzle_input):
    count = 0
    for values in puzzle_input:
        sum_sides = sum(values)
        max_side = max(values)
        if max_side < sum_sides - max_side:
            count += 1
    print(count)

def triangles_2(puzzle_input):
    count = 0
    column1 = []
    column2 = []
    column3 = []
    rearranged = []
    for values in puzzle_input:
        column1.append(values[0])
        column2.append(values[1])
        column3.append(values[2])
    rearranged.append(column1)
    rearranged.append(column2)
    rearranged.append(column3)
    # print(rearranged)
    for column in rearranged:
        for i in range(0,len(column),3):
            sum_sides = sum(column[i:i+3])
            max_side = max(column[i:i+3])
            if max_side < sum_sides - max_side:
                count += 1
    print(count)


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '\\' + 'day3.txt') as file:
        raw_input = file.readlines()
    puzzle_input = []
    for line in raw_input:
        puzzle_input.append(list(map(int, line.strip().split())))
    return puzzle_input

def main():
    puzzle_input = get_puzzle_input()
    triangles_1(puzzle_input)
    triangles_2(puzzle_input)

if __name__ == '__main__':
    main()
