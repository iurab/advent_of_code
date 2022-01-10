import os

def bathroom_code_1(puzzle_input):
    numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    moves = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    code = []
    for instructions in puzzle_input:
        # Start position -> 5
        x, y = 1, 1
        for direction in instructions:
            next_x = x + moves[direction][0]
            next_y = y + moves[direction][1]
            if 0 <= next_x < len(numpad) and 0 <= next_y < len(numpad):
                x = next_x
                y = next_y
        code.append(numpad[x][y])
    print(''.join(list(map(str, code))))

def bathroom_code_2(puzzle_input):
    numpad = [['0', '0', '1', '0', '0'], ['0', '2', '3', '4', '0'], ['5', '6', '7', '8', '9'], ['0', 'A', 'B', 'C', '0'], ['0', '0', 'D', '0','0']]
    moves = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    code = []
    for instructions in puzzle_input:
        # Start position -> 5
        x, y = 2, 0
        for direction in instructions:
            next_x = x + moves[direction][0]
            next_y = y + moves[direction][1]
            if 0 <= next_x < len(numpad) and 0 <= next_y < len(numpad) and numpad[next_x][next_y] != '0':
                x = next_x
                y = next_y
        code.append(numpad[x][y])
    print(''.join(code))

def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '\\' + 'day2.txt') as file:
        raw_input = file.readlines()
    puzzle_input = []
    for line in raw_input:
        puzzle_input.append(list(line.strip()))
    return puzzle_input

def main():
    puzzle_input = get_puzzle_input()
    bathroom_code_1(puzzle_input)
    bathroom_code_2(puzzle_input)

if __name__ == '__main__':
    main()
