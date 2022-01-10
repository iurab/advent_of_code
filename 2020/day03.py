from math import prod

def get_input():
    with open('input') as file:
        lines = file.readlines()
    slope = [list(line.strip()) for line in lines]
    return slope

def part01(slope):
    i = j = 0
    trees = 0
    while i < len(slope):
        if slope[i][j] == '#':
            trees += 1
        i += 1
        j = (j + 3) % len(slope[0])
    print(trees)

def part02(slope):
    trees = [0, 0, 0, 0, 0]
    traverses = [
        {'right': 1, 'down': 1},
        {'right': 3, 'down': 1},
        {'right': 5, 'down': 1},
        {'right': 7, 'down': 1},
        {'right': 1, 'down': 2}
    ]
    for index, traverse in enumerate(traverses):
        i = j = 0
        while i < len(slope):
            if slope[i][j] == '#':
                trees[index] += 1
            i += traverse['down']
            j = (j + traverse['right']) % len(slope[0])
    print(prod(trees))

slope = get_input()
part01(slope)
part02(slope)