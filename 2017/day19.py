import string


def help_packet(puzzle_input):
    map_ = puzzle_input
    direction = 'd'
    moves = {'u': [-1, 0], 'd': [1, 0], 'l': [0, -1], 'r': [0, 1]}
    pos = [0, 0]
    # Find entry
    pos[1] = map_[0].index('|')
    checkpoints = ''
    # Track seen positions
    seen = []
    while True:
        i, j = pos
        # Check if end of road
        if map_[i][j] == ' ':
            break
        # Save current position
        seen.append(pos)
        # Check if packet is on top of letter
        if map_[i][j] in string.ascii_uppercase:
            checkpoints += map_[i][j]
        elif map_[i][j] == '+':
            # Change direction
            for poss_dir in moves:
                next_move = [x + y for x, y in zip(pos, moves[poss_dir])]
                if next_move in seen:
                    continue
                x, y = next_move
                if map_[x][y] != ' ':
                    direction = poss_dir
                    break
        # # Remove current character
        # map_[i][j] = ' '
        # Go to next position
        pos = [x + y for x, y in zip(pos, moves[direction])]
    print(checkpoints)
    print(len(seen))


def get_puzzle_input():
    with open('day19.txt', 'r') as file:
        puzzle_input = file.readlines()
    return puzzle_input


def main():
    puzzle_input = get_puzzle_input()
    help_packet(puzzle_input)


if __name__ == '__main__':
    main()
