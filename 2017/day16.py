import os


def do_dance_moves(puzzle_input):
    # Generate programs list
    programs = [chr(i) for i in range(97, 97 + 16, 1)]
    dance_moves = puzzle_input.split(',')
    while True:
        for move in dance_moves:
            # Spin
            if move[0] == 's':
                steps = int(move[1:])
                programs = programs[-steps:] + programs[:-steps]
            # Exchange
            elif move[0] == 'x':
                positions = list(map(int, move[1:].split('/')))
                pos_0, pos_1 = positions
                programs[pos_0], programs[pos_1] = programs[pos_1], programs[
                    pos_0]
            # Partner
            else:
                elements = move[1:].split('/')
                pos_0 = programs.index(elements[0])
                pos_1 = programs.index(elements[1])
                programs[pos_0], programs[pos_1] = programs[pos_1], programs[
                    pos_0]
        yield programs


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '/' + 'day16.txt', 'r') as file:
        puzzle_input = file.read()
    return puzzle_input


def main():
    puzzle_input = get_puzzle_input()
    dance = do_dance_moves(puzzle_input)
    standings = [''.join([chr(i) for i in range(97, 97 + 16, 1)])]
    for _ in range(1000000000):
        programs_standing = next(dance)
        if ''.join(programs_standing) in standings:
            break
        else:
            standings.append(''.join(programs_standing))
    print(standings[0])
    print(standings[1000000000 % len(standings)])


if __name__ == '__main__':
    main()
