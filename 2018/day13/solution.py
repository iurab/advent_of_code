import numpy as np
import itertools

Ln, Col = 150, 150

MOVE = {'<': [0, -1], '^': [-1, 0], '>': [0, 1], 'v': [1, 0]}

DIRECTION = {
    '<': {
        'LEFT': 'v',
        'STRAIGHT': '<',
        'RIGHT': '^',
        '/': 'v',
        '-': '<',
        '\\': '^'
    },
    '^': {
        'LEFT': '<',
        'STRAIGHT': '^',
        'RIGHT': '>',
        '/': '>',
        '|': '^',
        '\\': '<'
    },
    '>': {
        'LEFT': '^',
        'STRAIGHT': '>',
        'RIGHT': 'v',
        '/': '^',
        '-': '>',
        '\\': 'v'
    },
    'v': {
        'LEFT': '>',
        'STRAIGHT': 'v',
        'RIGHT': '<',
        '/': '<',
        '|': 'v',
        '\\': '>'
    }
}


class Cart():
    def __init__(self, position, direction):
        self.position = position
        self.turn = itertools.cycle(['LEFT', 'STRAIGHT', 'RIGHT'])
        self.direction = direction

    def next_turn(self):
        return next(self.turn)


def get_input():
    # Take info from input file
    lines = open('input').read().splitlines()
    # Create matrix for chars
    tracks = np.chararray((Ln, Col), unicode=True)
    # Fill matrix with info
    for line, text in enumerate(lines):
        tracks[line, 0:] = list(text)
    return tracks


def find_crash(carts):
    crash_pos = []
    for cart1, cart2 in itertools.combinations(carts, 2):
        if cart1.position == cart2.position:
            crash_pos.append(cart1.position)
            print(cart1.position[1], cart1.position[0])
    return crash_pos


def print_tracks(tracks, carts):
    p_tracks = np.copy(tracks)
    for cart in carts:
        x, y = cart.position
        if p_tracks[x, y] == '>' or p_tracks[x, y] == '<' or p_tracks[x, y] == 'v' or p_tracks[x, y] == '^':
            p_tracks[x, y] = 'X'
        else:
            p_tracks[x, y] = cart.direction
    string = ''
    for row in p_tracks:
        string += ''.join(row)
        string += '\n'
    print(string)


def crash_pos(tracks):
    ## PART01
    # Find position for carts
    pos_carts = np.where((tracks == '<') | (tracks == '^') | (tracks == '>')
                         | (tracks == 'v'))
    # Create object for each position found
    carts = []
    for i in range(len(pos_carts[0])):
        x, y = pos_carts[0][i], pos_carts[1][i]
        cart = Cart((x, y), tracks[x, y])
        carts.append(cart)
        if cart.direction == '<' or cart.direction == '>':
            tracks[x, y] = '-'
        else:
            tracks[x, y] = '|'
    # Start movement
    while True:
        # Sort carts - top - down, left - right
        carts = sorted(carts, key=lambda x: (x.position[0], x.position[1]))
        # Move each cart
        for cart in carts:
            x, y = cart.position
            if tracks[x, y] == '+':
                c_turn = cart.next_turn()
                c_dir = cart.direction
                new_dir = DIRECTION[c_dir][c_turn]
                cart.position = [x + MOVE[new_dir][0], y + MOVE[new_dir][1]]
                cart.direction = new_dir
            else:
                c_dir = cart.direction
                new_dir = DIRECTION[c_dir][tracks[x, y]]
                cart.position = [x + MOVE[new_dir][0], y + MOVE[new_dir][1]]
                cart.direction = new_dir
        # Just to print for small examples
        # print_tracks(tracks, carts)
        # input()
        crashes = find_crash(carts)
        ## Only for PART01
        # if crash:
        #     print(crash)
        #     break
        # Remove crashed carts
        if crashes:
            to_remove = []
            for crash in crashes:
                for cart in carts:
                    if cart.position == crash:
                        to_remove.append(cart)
            for rem in to_remove:
               carts.remove(rem)
            if len(carts) == 1:
                print(carts[0].position)
                break


if __name__ == '__main__':
    tracks = get_input()
    # print(tracks)
    crash_pos(tracks)
