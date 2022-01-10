import os

def exit_maze_1(jump_offsets):
    # Initialize  values
    steps = 0
    position = 0
    while 0 <= position < len(jump_offsets):
        jump = jump_offsets[position]
        jump_offsets[position] += 1
        position += jump
        steps += 1
    print(steps)

def exit_maze_2(jump_offsets):
    # Initialize  values
    steps = 0
    position = 0
    while 0 <= position < len(jump_offsets):
        jump = jump_offsets[position]
        if jump < 3:
            jump_offsets[position] += 1
        else:
            jump_offsets[position] -= 1
        position += jump
        steps += 1
    print(steps)

def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '\\' + 'day5.txt') as file:
        puzzle_input = file.read ()
    puzzle_input = list(map(int, puzzle_input.split()))
    return puzzle_input

def main():
    jump_offsets = get_puzzle_input()
    init = jump_offsets[:]
    exit_maze_1(jump_offsets)
    print(init == jump_offsets)
    exit_maze_2(jump_offsets)

if __name__ == '__main__':
    main()