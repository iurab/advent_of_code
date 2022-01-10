import os
import operator

# https://www.redblobgames.com/grids/hexagons/

def hex_ed(puzzle_input):
    move = {'n': [1, 0, -1], 'ne': [1, -1, 0], 'se': [0, -1, 1], 's': [-1, 0, 1], 'sw': [-1, 1, 0], 'nw': [0, 1, -1]}
    position = [0, 0, 0]
    max_distance = 0
    for step in puzzle_input:
        # Change position by applying next move (+)
        position = list(map(operator.add, position, move[step]))
        current_distance = distance(position)
        if max_distance < current_distance:
            max_distance = current_distance
    # Distance
    print('Final distance', distance(position))
    print('Max distance', max_distance)

def distance(position):
    return int((abs(position[0]) + abs(position[1]) + abs(position[2]))/2)

def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '\\' + 'day11.txt') as file:
        raw_input = file.read()
    puzzle_input = raw_input.strip().split(',')
    return puzzle_input

def main():
    puzzle_input = get_puzzle_input()
    hex_ed(puzzle_input)


if __name__ == '__main__':
    main()
