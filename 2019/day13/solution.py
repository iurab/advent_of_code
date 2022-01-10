from collections import defaultdict
from intcode import IntCode

ball = None
paddle = None


def get_input():
    with open('input') as file:
        line = file.readline().split(',')
    data = defaultdict(int)
    for pos, x in enumerate(line):
        data[pos] = int(x)
    return data


def render(tiles):
    elements = [[' '] * 40 for _ in range(20)]
    for pos in tiles:
        x,y = pos
        if tiles[pos] == 1:
            elements[y][x] = '*'
        elif tiles[pos] == 2:
            elements[y][x] = '#'
        elif tiles[pos] == 3:
            elements[y][x] = '='
        elif tiles[pos] == 4:
            elements[y][x] = 'o'
    screen = '\n'.join(''.join(line) for line in elements)
    print(screen)


def part01():
    opcodes = get_input()
    computer = IntCode(opcodes)
    screen = {}
    while not computer.done:
        x = computer.run()
        y = computer.run()
        tile = computer.run()
        if not computer.done:
            screen[(x,y)] = tile
    tiles = list(screen.values())
    print(tiles.count(2))
    print(list(screen.keys()))


def paddle_move():
    global ball
    global paddle
    if ball[0] < paddle[0]:
        return -1
    elif ball[0] > paddle[0]:
        return 1
    else:
        return 0


def part02():
    global ball
    global paddle
    opcodes = get_input()
    computer = IntCode(opcodes, paddle_move)
    computer.set_address(0, 2)
    tiles = {}
    score = 0
    while not computer.done:
        x = computer.run()
        y = computer.run()
        tile = computer.run()
        if not computer.done:
            tiles[(x,y)] = tile
            paddle = (x,y) if tile == 3 else paddle
            ball = (x,y) if tile == 4 else ball
            score = tile if x == -1 else score
    print(score)

part01()
part02()